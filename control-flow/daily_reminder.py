# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Customized reminder based on priority and time sensitivity
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task")
    case "low":
        print(f"Reminder: '{task}' is a low priority task")
    case _:
        print(f"Reminder: '{task}' has an unknown priority level")

# Append time-sensitive message
if time_bound == "yes":
     print(f" that requires immediate attention today!")
else:
    if priority in ["low", "medium", "high"]:
        print(f". Consider planning accordingly.")