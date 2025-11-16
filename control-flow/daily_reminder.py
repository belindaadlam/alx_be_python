# daily_reminder.py

# 1. Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the base reminder message
base_reminder = ""

# 2. Use Match Case to set the base message based on priority
match priority:
    case 'high':
        # High priority tasks will be checked for time-bound status later
        base_reminder = f"'{task}' is a {priority} priority task"
    case 'medium':
        # Medium priority tasks will also be checked for time-bound status later
        base_reminder = f"'{task}' is a {priority} priority task"
    case 'low':
        # Low priority tasks get their full message immediately
        base_reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
    case _:
        # Handle invalid priority input
        print("Invalid priority entered. Using 'medium' priority by default.")
        base_reminder = f"'{task}' is a medium priority task"

# 3. Use an if statement to modify the reminder if the task is time-bound
# We only add the 'immediate' text if it's time-bound AND it wasn't a low priority task.
if time_bound == 'yes' and priority in ['high', 'medium']:
    # The requirement is to add: 'that requires immediate attention today!'
    base_reminder += " that requires immediate attention today!"

# 4. Print the final customized reminder
print(f"\nReminder: {base_reminder}")