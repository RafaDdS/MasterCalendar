# Master Calendar
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
Ask me for the credentials.json of the Master Calendar and you shall receive. Without it you will need to make your own GCP project and create new credentials. It doesn't seems dangerous to share, but I will try to keep it safe from the general public.

The first time you use the system it will open an additional login page, in this one you will login with the account you want to save the events to. The proper link will also be exposed in the terminal in case the page doesn't opens automatically. You will need to allow the system to make modifications to your calendar. The information is saved to the token.picke file, you may delete it if you want to change the calendar you are using.

A gmail login session will open on a new chrome window. Then you need to:
- Login with your account.
- It's always a good idea to close any popups that show up. They might lead to wrong results.
- Navigate to the email you want to process.
- Input "Vai" on the terminal to indicate to the script you want to process the current email.
- Input S to confirm the creation of the event with the captured information.
- Input "Sair" or a keyboard interrupt (Cntrl + C) on the terminal to indicate you want to halt the script. This will also close the chrome window.