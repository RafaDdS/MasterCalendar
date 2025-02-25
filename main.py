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
			print(text)
			##re.match(text, r"")

		elif command == "Sair":
			driver.quit()
			break

	except NoSuchElementException:
		continue