print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
choice1 = input(
    "You are at a cross road. Do yu want to go left or right.Type R for right and L of left\n"
)
if choice1 == "L":
    choice2 = input(
        "You came to a lake. There is a island in the middle of the lake. Do you want to swin or wait for the boat. Type W to wait and S to swim.\n"
    )
    if choice2 == 'W':
        choice3 = input(
            "You discover 3 doors on that island. One of them will led you the treasure. The door colors are red,blue,yellow. Type RE for red color, B for blue color and Y for yellow color\n"
        )
        if choice3 == "RE":
            print("You fell in fire. Game Over")
        elif choice3 == "B":
            print("You were killed by wild animal. Game Over")
        elif choice3 == "Y":
            print("Congrajulations!!!You discovered the treasure")
    else:
        print("You drowned. Game Over")
else:
    print("You fell in a hole. Game Over")
