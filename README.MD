# CLI Todo Python Project with Scheduling and SMS Sending

This Python project is a Command-Line Interface (CLI) Todo application with scheduling capabilities and SMS sending functionality. It allows users to manage their tasks, set priorities, schedule them, and receive reminders via SMS.

The project is divided into two main files:
1. **SMS_Sender.py**: Handles the SMS sending functionality and scheduling logic.
2. **Todo_app.py**: Contains the main logic for the Todo application and the option to run SMS sending functionality as a daemon.

![Screenshot](imgs/s1.png.png)

![Screenshot](imgs/s2.png.png)

![Screenshot](imgs/s3.png.png)


## Installation

### Prerequisites
- Python 3.x
- Twilio account (for SMS sending)
- Docker (optional)

### Setup
1. Clone this repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Set up your Twilio account and obtain your ACCOUNT_SID and AUTH_TOKEN.
4. Create a `.env` file and set the `ACCOUNT_SID` and `AUTH_TOKEN` environment variables.
5. Run the application using `python Todo_app.py`.

## Usage

### Commands
- `add_todo`: Add a new todo with optional priority.
- `edit_todo`: Edit an existing todo.
- `list_todos`: List all todos or a specific todo.
- `delete_todos`: Delete a todo by index.
- `delete_all`: Delete all todos.
- `schedule_todo`: Schedule a todo.
- `about`: About the application.

### Example Usage
```bash
# Add a new todo
python Todo_app.py add-todo "Finish project" --priority= "m"

# List all todos
python Todo_app.py list-todos

# Schedule a todo
python Todo_app.py schedule-todo -i 0 --date "2024-03-20 10:00"

# Delete a todo
python Todo_app.py delete-todos --index 0

# Edit a todo
python Todo_app.py edit-todo -i <index> "<new_todo_text>" --priority=<new_priority> --date=<new_date>

```

## Docker

-To run the project using Docker, follow these steps:

```bash
docker build -t todo-app .
docker run --env ACCOUNT_SID="YOUR_ACCOUNT_SID" --env AUTH="YOUR_AUTH_TOKEN" todo-app

```

## Disclaimr

This project is still an expiremental release, I am still testing it, it might contain some bugs, I wanted to share it with the community, so feel free to use it, modify it and improve it as you like. Happy Coding!


## Contributors

Ilyes Chaabane


## Acknowledgments

Thanks to Twilio for their SMS API.
Feel free to contribute to this project by forking it and submitting pull requests!
