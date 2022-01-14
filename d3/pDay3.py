print('''
                        _._
                               .-~ | ~-.
                               |   |   |
                               |  _:_  |                    .-:~--.._
                             .-"~~ | ~~"-.                .~  |      |
            _.-~:.           |     |     |                |   |      |
           |    | `.         |     |     |                |   |      |
  _..--~:-.|    |  |         |     |     |                |   |      |
 |      |  ~.   |  |         |  __.:.__  |                |   |      |
 |      |   |   |  |       .-"~~   |   ~~"-.              |   |      |
 |      |   |  _|.--~:-.   |       |       |         .:~-.|   |      |
 |      A   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
 |      M   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      C   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      9   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      9   | |      |   | |       |  |   |     |  |  |   |   |      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

''')


print("Welcome to Treasure City.\n Your mission is to find the reasure")



roadToGo = input(print("You are at a crossroad,  where do you want to go?? L or R\n"))

if roadToGo == "L":
    
    swimWait = input("Dou you want to swim or wait???: S or W")
    
    if swimWait == "W":
        door = input("You have to open a door, which R, B or Y?")
        
        if door == "R":
            print("Burned by fire. Game Over.")
        elif door == "B":
            print("Eaten by beasts. Game Over")
        elif door == "Y":
            print("YOU WIN!!!!!")
        else:
            print("Game over :( ")
    else:
        print("Attacked by trout. Game over")

else:
    print("Fall into a hole. Game Over.")








