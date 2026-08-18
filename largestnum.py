a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if a > b and a > c:  # Checking whether a is the largest number
    print("a is the largest number:", a)

elif b > c:  # Checking whether b is the largest number
    print("b is the largest number:", b)

else:  # Otherwise, c is the largest number
    print("c is the largest number:", c)