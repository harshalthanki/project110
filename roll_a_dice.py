import random

input = "y"

while input == "y": 

    number = random.randint(1,6)  

    if number == 1: 
        print("[       ]")
        print("[   0   ]")
        print("[       ]")
        print("Number: 1")

    if number == 2: 
        print("[       ]")
        print("[  0 0  ]")
        print("[       ]")
        print("Number: 2")

    if number == 3: 
        print("[       ]")
        print("[ 0 0 0 ]")
        print("[       ]")
        print("Number: 3")

    if number == 4: 
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]")
        print("Number: 4")

    if number == 5: 
         print("[ 0   0 ]")
         print("[   0   ]")
         print("[ 0   0 ]")
         print("Number: 5") 

    if number == 6: 
        print("[ 0   0 ]")
        print("[ 0   0 ]")
        print("[ 0   0 ]")
        print("Number: 6") 
             
    input=input("press y to roll again and n to exit:") 