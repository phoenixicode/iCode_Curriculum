from easytello import tello
tell = tello.Tello()
print("""
      w = forward 
      s = backward
      a = left
      d = right
""")
tell.takeoff()
ab = True
while ab:
    z = input("enter the commands: ")
    if z == "w":
        tell.forward()
    elif z == "s":
        tell.back()
    elif z == "a":
        tell.left()
    elif z == "d":
        tell.right()
    elif z == "q":
        tell.land()
        ab = False
        break
    else:
        print("invalid keys ")
        ab = False
        break


