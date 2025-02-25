# MasterCalendar
 Script to automate PESC emails to Google calendar.

 This is a quick project to solve a very specific problem. I want an automation to convert emails about master and doctorate presentations to events in my google calendar.

 ## You will need
- Python 3.12
- Chrome Browser
- pipenv

 ## How to use
  Open the main folder on a terminal and run:
```
  pipenv install
  pipenv run python main.py
```
  A gmail login session will open on a new chrome window. Then you need to:
  - Login with your account.
  - It's always a good idea to close any popups that show up. They might lead to wrong results.
  - Navigate to the email you want to process.
  - Input "Vai" on the terminal to indicate to the script you want to process the current email.
  - Input "Sair" on the terminal to indicate you want to halt the script. This will also close the chrome window.