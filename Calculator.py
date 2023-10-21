# <---------- Calculator ------------>
num1 = int(input("Enter First  Number = "))
op = input("Enter Operation = ")
num2 = int(input("Enter Second Number = "))
if op == '+':
    print("Successfully Run")
    print("Addition = ",(num1+num2))
elif op == '-':
    print("Successfully Run")
    print("Subtraction = ",(num1-num2))
elif op == '*':
    print("Successfully Run")
    print("Multiplication = ",(num1*num2))
elif op == '/':
    print("Successfully Run")
    print("Division = ",(num1/num2))
elif op == "squar":
    print("Successfully Run")
    print("Squar = ",(num1**2))
elif op == '%':
    print("Successfully Run")
    print("Reminder = ",(num1%num2))
else:
    print("Something missing! Please Try Again ")

       ''' Thank You Every one '''