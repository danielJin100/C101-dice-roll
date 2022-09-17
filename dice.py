import random

ifRoll = "y"

while ifRoll=="y":
    roll = random.randint(1, 6)
    print("[-----]")

    if(roll == 1):
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    if(roll == 2):
        print("[     ]")
        print("[0   0]")
        print("[     ]")
    if(roll == 3):
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
    if(roll == 4):
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    if(roll == 5):
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    if(roll == 6):
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
    print("[-----]")
    print(roll)
    ifRoll = input("Roll again? [y/n]")

