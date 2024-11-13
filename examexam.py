age = int(input("Enter your age: "))
attendance = int(input("Enter your attendance in %: "))
marks = int(input("Enter your marks in %: "))

if age >= 18 and attendance >= 80 and marks >= 80:
    print("Eligible.")
else:
    print("Not eligible.")