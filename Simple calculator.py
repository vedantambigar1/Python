select = input("select operator (+,-,*,/):") # sellection of operator

x = int(input("enter first number:"))
y = int(input("enter second number:"))
# taking two number from user and storing it in x and y variable

if select == "+": #addition
    print(x + y)

if select == "-": # subtraction
    print(x - y)

if select == "*": # multiplication
    print(x * y)

if select == "/": # division
    if y != 0: # checking werhter the second number is zero or not
        print(x / y) # if it is not zero then x divide by b is possible
    else:
        print("error ! division cannot be done by zero") # if it is zero then it will print error message
        
    