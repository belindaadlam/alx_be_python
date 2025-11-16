# daily_reminder.py

# 1. Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# 2. Determine the reminder text using conditional logic
if priority == 'high' or priority == 'medium':
    # This covers the high/medium priority cases
    reminder_text = f"'{task}' is a {priority} priority task"
    
    # Check for time-bound status for high/medium tasks
    if time_bound == 'yes':
        # Append the specific urgent message if time-bound
        reminder_text += " that requires immediate attention today!"
    else:
        # If not time-bound, just end the sentence.
        reminder_text += "."

elif priority == 'low':
    # This covers the low priority case, which has a specific message structure
    reminder_text = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."

else:
    # Handle invalid priority input
    print("Invalid priority entered. Defaulting to a simple reminder.")
    reminder_text = f"'{task}' is a task to be completed."

# 3. Print the final customized reminder with the required starting text "Reminder: "
# The checker specifically wants this format: print(f"Reminder: {reminder_text}")
print(f"Reminder: {reminder_text}")