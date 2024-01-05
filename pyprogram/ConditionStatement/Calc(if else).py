print('''
       + Add
       - Subtract
       * Multiply
       / Divide
''')
num1 = int(input("Enter the value\n: 1"))
num2 = int(input("Enter the value\n: 2"))
opr = input("Enter the Opr..")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invaild /opr")

