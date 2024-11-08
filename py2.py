def introduction(Username):
    print("Hello, my name is", Username)

    
name = input("Enter your name: ")
introduction(name)

# Recursion

def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1) 

n = int(input("Enter a number: "))

if n < 0:
    print("The factorial of negative numbers does not exist.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    print("The factorial of ",n, " is ",factorial(n))
    
# Calculation

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

x = int(input("Input the first number."))
y = int(input("Input the second number."))

print("Sum: ", add(x, y))
print("Difference: ", subtract(x, y))
print("Product: ", multiply(x, y))
print("Quotient: ", divide(x, y))
