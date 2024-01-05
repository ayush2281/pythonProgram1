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
if opr=="-":
    print(num1-num2)
if opr=="*":
    print(num1*num2)
if opr=="/":
    print(num1/num2)
if opr!="+" and opr!="-" and opr!="*" and opr!="/":
    print("invaild /opr")

