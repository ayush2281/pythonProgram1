# factorial of number

# num = int(input("Enter the no to find the fact :"))
# factorial = 1

# if num == 0:
#     print("the fact of 0 is 1")
#
# else:
#     for i in range(1, num+1):
#         factorial = factorial*i
#     print("the factorial of ", num, 'is',factorial)


# factorial function

def factorial_value(num):
    factorial = 1

    if num == 0:
        return factorial
    else:
        for i in range(1, num+1):
            factorial = factorial*i
        return  factorial
print(factorial_value(5))