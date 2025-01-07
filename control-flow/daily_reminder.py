task = input("Enter your task:")
priority = input("Priority (high/medium/low):").strip().lower()
time = input("Is it time-bound? (yes/no):").strip().lower()
match priority:
    case "high":
        if time == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a low priority task. consider completing it when you have free time.")
    case "medium":
        if time == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a low priority task. consider completing it when you have free time.")
    case "low":
        if time == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a low priority task. consider completing it when you have free time.")
    case _:
        print("Incalid input")