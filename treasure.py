# Define the new decoration as a variable
decoration = '''
==================================================
'''

ascii_art = ('''
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
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************
'''
"\n* Welcome to the TREASURE ISLADE game! *\n There is a treasure that waiting only for you!\nֿ")
print(ascii_art)
print(f'{decoration}\n                * Level 1 *\n{decoration}')
level1 = input('Were do you going to turn, "left" or "right": ').lower()
#print(start)

if level1 == "right":
    print(f'{decoration}\n                * Level 2 *\n{decoration}')
    level2 = input("You came into a dark hall. What are you going to do now? Ask for way out/Take a torch - type 'ask' or 'take':").lower() # type: ignore

    if level2 == "take":
        print(f'{decoration}\n                * Level 3 *\n{decoration}')
        level3 = input("You came to a river bank. What do you chose? swim to the islande/Wait for a boat - type 'swim' or 'wait': ").lower()

        if level3 == "wait":
            print(f'{decoration}\n                * Level 4 *\n{decoration}')
            level4 = input("You came to the islande, there is a small home in front of you. You came into the house. There is a 3 doors in front of you. \nWich color you will pick? type 'red' or 'yellow' or 'green': ").lower()
            if level4 == "yellow":
                print("CONGRATULATIONS! you fined the treasure! Game over.")           
            elif level4 == "red":
                print("You enterd to a burning room. Game over.")           
            elif level4 == "green":
                print("You enterd to a room full of poisonous gas. Game over")
        
        elif level3 == "swim":
            print("You were eaten by crocodiles. Game over.")
    
    elif level2 == "ask":
        print("you were bitten by a poisonous snake. Game over.")
elif level1 == "left":
    print("you fall into a hole. Game over.")
