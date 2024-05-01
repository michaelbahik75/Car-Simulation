# Building Simulation Car Game
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped...")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit the game
              ''')
    elif command == "quit":
        print("Are you sure to quit the game?[y/n]: ")
        exit = input().lower()
        if exit == 'n':
            print("enter the command: ")
        elif exit == 'y':
            break
    else:
        print("Invalid command")