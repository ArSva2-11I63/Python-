num = int(input("Enter a number: "))

if num == 0:
    print(0)
elif num < 0:
    print("Negative numbers do not have fibonacci series.")



num1 = 0
num2 = 1
count = 0
next = 1

while count < num:
    next = num1 + num2
    print(next, end=" ")
    num1 = num2
    num2 = next
    count = count + 1
