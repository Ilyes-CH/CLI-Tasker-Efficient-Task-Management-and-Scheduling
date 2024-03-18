#!/usr/bin/env python3

from twilio.rest import Client
import click
import tqdm
import time
import calendar
import schedule
import os
import sys
from dotenv import load_dotenv
import threading
from datetime import datetime


load_dotenv()

account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH"]
client = Client(account_sid, auth_token)

cal = calendar.TextCalendar()

def scan():
    with open("./To-Do-CLI/todos.txt", 'r') as f:
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

def start_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1) 

def SMS_sender(todos):
    for todo in todos:
      
        message = client.messages.create(
            from_="+19123197793",
            body=todo,
            to="+21656126611",
        )

        print(f"SID:{message.sid} \nStatus:{message.status}")


class Todo:
    def __init__(self, author, schedule):
        self.author = author
        self.schedule = schedule

    @staticmethod
    def initiate():
        global scan
        scan()

    @staticmethod
    def start_up():
        with open("todos.txt",'r') as f:
            todos_list = f.read().splitlines()
            
            for item in tqdm(todos_list, desc="Checking Available Todos And Schedules",unit="byte",colour="green"):
                time.sleep(0.1)
        
    
    def about(self):
        # provide author name tqdm launch bar
        click.echo("Welcome to the CLI version of a Todo App\n")
        click.echo("Version 1.0.0\n")
        click.echo(f"Author: {self.author} \n")
        click.echo("run main.py or main.py --help to see list of commands\n")
   
    @staticmethod
    def schedule_todo(schedule, idx):
        global cal
        cal_text = cal.formatmonth(datetime.now().year, datetime.now().month)

        print(cal_text)
        # send SMS for scheduled task
        with open("todos.txt", 'r') as f:
            todos_list = f.read().splitlines()
            l = len(todos_list[idx])
            task = todos_list[idx]

            if todos_list[idx][l - 25:-24] == "S":
                l_task = list(task)
                l_task[len(l_task) - 28:len(l_task)] = " "
                r = ("").join(l_task)
                r += f"| Schedule date: {schedule}"

                print(r)

                todos_list[idx] = r  # Update the list element

                with open("todos.txt", 'w') as f:  # Open in append mode after the loop
                    f.write('\n'.join(todos_list))
                    f.write("\n")
            else:
                  with open("todos.txt", 'r') as f:
                    todos_list = f.read().splitlines()
                    todos_list[idx]+=f" | Schedule date: {schedule}"
                  with open("todos.txt", 'w') as f:  # Open in append mode after the loop
                    f.write('\n'.join(todos_list))
                    f.write("\n")
        print(f"Task {idx} is scheduled for:", schedule)

Priorities=  {
     'l': "low",
      'm':"medium", 
      'h':"high",
      'p':"priority"
}

# Instantiate the class
todo_app = Todo('Ilyes Chaabane', 'Not Set Yet')

#add todos
@click.command()
@click.argument("todo")
@click.option('--priority', type= click.Choice(Priorities.keys()) ,help="Choose the degree of the priority of your task", default="m")
def add_todo(todo, priority):
   
    global index
    with open("todos.txt","a") as f:
        f.write(f"TODO: {todo} | Priority: {Priorities[priority]}\n")

    print(f'New Todo added {todo}, and priority is {Priorities[priority]}')

# edit todo
@click.command()
@click.option("-i", type=int, help="Index")
@click.argument("todo")
@click.option('--priority', type= click.Choice(Priorities.keys()) ,help="Choose the degree of the priority of your task")
@click.option('--date')
def edit_todo(i,todo,priority,date):
    '''
    you need to specify all the parameters to fully update the Todo Otherwise it will default to None
    '''
    with open("todos.txt","r") as f:
        todos_list = f.read().splitlines()
        print("OLD:    ",todos_list[i])
    # try except this with statement and add the star animation make exceptions for incomplete params in the command
        #  if priority is None:
            # for i, todo  in enumerate(todos_list):
                # print(f"({i}) - {todo}")
    with open("todos.txt",'w') as f:
        todos_list[i] = f"UPDATED TODO: {todo} | Priority: {Priorities[priority]} | schedule date: {date}"
        print("UPDATE: ",todos_list[i])
        f.write('\n'.join(todos_list)) 
        f.write("\n")      
        
    # check index then add todo regularly in the specific index and then call schedule task to reschedule it

#schedule todos
@click.command()
@click.option('-i', type=int)
@click.option('--date')
def schedule_todo(i,date):
    Todo.schedule_todo(date, i)


#list todos
@click.command()
@click.option("-i","--index", type=int)
def list_todos(index):
    with open("todos.txt",'r') as f:
        todos_list = f.read().splitlines()
        
    if len(todos_list) == 0:
        print("You have no todos for now")
    else:
        if index is None:
            for i, todo  in enumerate(todos_list):
                print(f"({i}) - {todo}")
        else:
            try:
                print(todos_list[index])
            except IndexError:
                print("WARNING: Your Index exceeds the lenght of the todos list check your todos file")
# delete all todos
@click.command()
def delete_all():
     with open("todos.txt",'r') as f:
            todos_list = f.read().splitlines()
            todos_list.clear()
     with open("todos.txt",'w') as f:
        f.write('\n'.join(todos_list))
        
     print("All todos are now removed")

#delete todos
@click.command()
@click.option("--index",type=int, prompt="Please Enter the Index Of the Task",help="When deleting we treat the todos list as a regular list so index starts from 0\nif you would like to modify the sourse code change the option to argument and set the required parameter to 1")
def delete_todos(index):
    
    try:
        if index is not None:
            with open("todos.txt",'r') as f:
                todos_list = f.read().splitlines()
                todos_list.pop(index)
            with open("todos.txt",'w') as f:
                f.write('\n'.join(todos_list))
                f.write('\n')
    
        print(f"Todo at index {index} is removed")
    except IndexError:
        click.echo("An error occurred while deleting the todo. Please check the index.")

    
def initiate_scan():
    todo_app.initiate()
    start_schedule()

#about the app
@click.command()
def about():
    todo_app.start_up()
   

# Grouping commands under a single Click group
@click.group()
def cli():
    pass

# Adding the commands to the Click group
cli.add_command(add_todo)
cli.add_command(schedule_todo)
cli.add_command(delete_todos)
cli.add_command(edit_todo)
cli.add_command(list_todos)
cli.add_command(delete_all)
cli.add_command(about)
# Call the click.command() decorated functions directly
if __name__ == '__main__':
    scan_thread = threading.Thread(target=initiate_scan, daemon=True)
    schedule.every().day.at("04:00").do(scan_thread.start)
    scan_thread.start()  # Start the thread
    cli()

