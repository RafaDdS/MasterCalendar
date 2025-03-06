from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event
from datetime import datetime
import re

driver = webdriver.Chrome()
driver.get("https://mail.google.com/mail")

calendar = GoogleCalendar(credentials_path="credentials.json")

while True:
	try:
		command = input()
		
		if command == "Vai":
			textElement = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[4]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]")
			text = textElement.text
			print(len(text))
			
			titleMatch = re.search(r"tulo: ([-\w/() :,]+)", text)
			linkMatch = re.search(r"Sala virtual:? ([\w:/.-]+)", text)
			roomMatch = re.search(r"Sala( presencial)?:? (?!virtual)([-\w ,]+)", text)
			DateTimeMatch = re.search(r"Data\/hora\/local:\n- (\d+)\/(\d+)(\/(\d+))?[^\d]*(\d+):?(\d*)h?", text)

			title = titleMatch.group(1) if titleMatch else "Sem título"
			link = linkMatch.group(1) if linkMatch else "Sem link"
			room = roomMatch.group(2) if roomMatch else "Sem sala"
			
			day = int(DateTimeMatch.group(1)) if DateTimeMatch and DateTimeMatch.group(1) else datetime.today().day
			month = int(DateTimeMatch.group(2)) if DateTimeMatch and DateTimeMatch.group(2) else datetime.today().month
			year = int(DateTimeMatch.group(4)) if DateTimeMatch and DateTimeMatch.group(4) else datetime.today().year
			hour = int(DateTimeMatch.group(5)) if DateTimeMatch and DateTimeMatch.group(5) else datetime.today().hour
			minute = int(DateTimeMatch.group(6)) if DateTimeMatch and DateTimeMatch.group(6) else datetime.today().minute

			eventDateTime = datetime(year, month, day, hour, minute)

			print("Título: ", title)
			print("Link: ", link)
			print("Sala: ", room)
			print("Horário: ", eventDateTime.strftime("%d/%m/%Y %H:%M"))

			ok = input("Isso mesmo? (S/N): ")

			if ok == "S" or ok == "s":
				event = Event(
					title,
					start=eventDateTime,
					description=f"Sala: {room}, Link: {link}",
					minutes_before_popup_reminder=60,
					color_id='8'
				)

				calendar.add_event(event)
				print("Evento adicionado.")
			else:
				print("Adição de evento cancelada.")

		elif command == "Sair":
			driver.quit()
			break

		else:
			print("Não entendi! Vai ou Sair")

	except NoSuchElementException:
		print("Element not found")

	except KeyboardInterrupt:
		driver.quit()
		break

#	except Exception as e:
#		print(e)
#		driver.quit()
#		break
