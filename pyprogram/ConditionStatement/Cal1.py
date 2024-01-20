print('''
       + Add
       - Subtract
       * Multiply
       / Divide
''')
num1 = int(input("Enter the first value\n"))
num2 = int(input("Enter the second value\n"))
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

