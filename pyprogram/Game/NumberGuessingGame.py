import random
Cnumber = random.randrange(1,1000)
userInput = int(input("Enter Your Number-->"))
if userInput>Cnumber:
    print("Computer Number",Cnumber)
    print("Your Guess Number Is High And Won The Game")
elif Cnumber>userInput:
     print("Computer Nuber", Cnumber)
     print("OOPS You loose the Game")

else:
    print("Computer Nuber",Cnumber)
    print("Your Guess Number is Equal")