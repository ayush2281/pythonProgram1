import random
Cnumber = random.randrange(1,101)
userInput = int(input("Enter Your Number-->"))
if userInput>Cnumber:
    print("Computer Number",Cnumber)
    print("Your Guess Number Is High And Won The Game")
elif Cnumber>userInput:
     print("Computer Nuber", Cnumber)
     print("Your Guess Number Is low And You Loose The Game")

else:
    print("Computer Nuber",Cnumber)
    print("Your Guess Number is Equal")