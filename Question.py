#Wap to check if a number entered by the user is odd or even

num = int(input("Enter a number:"))

if (num % 2 == 0):
    print("Even")

else:
    print("Odd")


#Wap to find the greatest of the 3 numbers entered by the user.

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

if ( a >= b and a >= c):
    print("First Number is largest", a)

elif (b >= c):
    print("Second number is largest", b)

else:
    print("third number is largest", c)


#Wap to check if a number is a multiple of 7 or not

num = int(input("Enter a number: "))

if (num % 5 == 0):
    print("Multiple of 5")

else:
    print("Not a multiple")