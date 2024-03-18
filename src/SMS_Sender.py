from twilio.rest import Client
import time
import schedule
from datetime import datetime
# import os

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

def SMS_sender(todos):
    for todo in todos:
      
        message = client.messages.create(
            from_="+19123197793",
            body=todo,
            to="",
        )

        print(f"SID:{message.sid} \nStatus:{message.status}")

def scan():
    with open("todos.txt", 'r') as f:
        todos_list = f.read().splitlines()

    today = datetime.now().strftime("%d/%m/%Y")
    todos_for_today = [todo for todo in todos_list if todo.endswith(today)]

    if todos_for_today:
        print(f"Sending todos for {today}:")
        for todo in todos_for_today:
            print(todo)
        SMS_sender(todos_for_today)
    else:
        print("No todos for today.")

if __name__ == "__main__":
    schedule.every().day.at("04:00").do(scan)  # Schedule the scanning job to run every day at 19:45

    while True:
        schedule.run_pending()
        time.sleep(1)
