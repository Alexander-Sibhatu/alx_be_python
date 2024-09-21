Task = input("Enter your task:")
Priority = input("What is the priority of this task (high, medium, low)").lower()
Time_bound = input("Is it time bounded (yes/no)").lower()

 
match Priority:
    case "high":
        reminder = f"'{Task}' is a high priority task"
    case "medium":
        reminder = f"'{Task}' is a medium priority task"
    case "low":
        reminder = f"'{Task}' is a low priority task"
if Time_bound == 'yes':
    reminder += " that requires immediate attention today!"
if Time_bound == 'no' and Priority in ["medium", "low"]:
    reminder += ". Consider completing it when you have free time."

print(reminder)