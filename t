def function1(n):
    result = n*(n+1)/2
    print(result)

num = int(input("Enter a number: "))
function1(num)
print()

def function2(n):
    sum = 0
    for i in range (1, n+1):
        sum = i + sum
    return sum
    
    
num2 = int(input("Enter a number: "))
print(function2(num2))
print()

def function3(n):
    sum = 0
    for i in range (1, n+1):
        for j in range (1, i+1):
            sum = 1 + sum
    return sum

num3 = int(input("Enter a number: "))
print(function3(num3))
print()
