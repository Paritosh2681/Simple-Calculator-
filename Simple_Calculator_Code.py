def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
def pow(x,y):
    return x**y
def sqrt(x):
    return x**0.5
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
def calculation():
    print("Select operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Power")
    print("7.Square root")
    print("8.Factorial")
    choice = input("Enter choice(1/2/3/4/5/6/7/8):")
    num1 = float(input("Enter first number: "))
    if choice != '7' and choice != '8':
        num2 = float(input("Enter second number: "))
    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))
    elif choice == '2':
        print(num1,"-",num2,"=", sub(num1,num2))
    elif choice == '3':
        print(num1,"*",num2,"=", mul(num1,num2))
    elif choice == '4':
        print(num1,"/",num2,"=", div(num1,num2))
    elif choice == '5':
        print(num1,"%",num2,"=", mod(num1,num2))
    elif choice == '6':
        print(num1,"^",num2,"=", pow(num1,num2))
    elif choice == '7':
        print("Square root of",num1,"=", sqrt(num1))
    elif choice == '8':
        print("Factorial of",num1,"=", fact(num1))
    else:
        print("Invalid input") 
calculation()
while True:
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation == 'yes':
        calculation()
    else:
        print("Thank you for using the calculator")
        break