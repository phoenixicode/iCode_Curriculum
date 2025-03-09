from easytello import tello
Drone = tello.Tello()
print("""
        w-forward
        s-backward
        a-left
        d-right
        q-land
    """)
Drone.takeoff()
Flag = True
while Flag:
    command = input("Enter your command: \n")
    if command == "w":
        Drone.forward(100)
    elif command == "s":
        Drone.back(100)
    elif command == "a":
        Drone.left(100)
    elif command == "d":
        Drone.right(100)
    elif command == "q":
        Drone.land()
        Flag = False
        break
    else:
        print("Invalid Command")
        Drone.land()
        Flag = False
        break
