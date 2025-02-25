from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re

driver = webdriver.Chrome()
driver.get("https://mail.google.com/mail")

while True:
	command = input()

	try:
		if command == "Vai":
			textElement = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[4]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]")
			text = textElement.text
			print(len(text))
			
			titleMatch = re.search(r"tulo: ([\w/() :,]+)", text)
			linkMatch = re.search(r"Sala virtual: ([\w:/.-]+)", text)
			roomMatch = re.search(r"Sala( presencial)*: ([\w-]+)", text)
			DateTimeMatch = re.search(r"Data\/hora\/local:\n- (\d+\/\d+(\/\d+)?)[^\d]*(\d+:*\d*h?)", text)

			title = titleMatch.group(1) if titleMatch else ""
			link = linkMatch.group(1) if linkMatch else ""
			room = roomMatch.group(2) if roomMatch else ""
			date = DateTimeMatch.group(1) if DateTimeMatch else ""
			time = DateTimeMatch.group(3) if DateTimeMatch else ""

			print("Título: ", title)
			print("Link: ", link)
			print("Sala: ", room)
			print("Data: ", date)
			print("Hora: ", time)

		elif command == "Sair":
			driver.quit()
			break

		else:
			print("Não entendi! Vai ou Sair")

	except NoSuchElementException:
		print("Element not found")

	except Exception as e:
		print(e)
		driver.quit()
		break
