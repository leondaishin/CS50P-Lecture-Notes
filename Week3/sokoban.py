def main(): 
    history = []

    while True: 
        action = input("Action: ")

        if action == "undo": 
            #erase the last input from the history list.
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart": 
            history.clear()
            print("Game restarted. ")
        else:
            history.append(action)
        




main()