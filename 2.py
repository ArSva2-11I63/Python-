#bmi

height = float (input("Enter your height in cm. "))
weight = float (input("Enter your weight in kg. "))

bmi = weight/(height/100)**2

print (bmi)

if bmi <= 18.4:
    print("Underweight")

elif bmi <= 24.9:
    print("Normal")    

elif bmi <= 29.9:
    print("Overweight")

elif bmi <= 34.9:
    print("Severely Overweight")

elif bmi <= 39.9:
    print("Obese")

else:
    print("Severely Obese")                


#even / odd

num = int (input("Enter a number: "))
if num % 2 == 0:
    print("The number is even ")
    
    if num <= 60:
        print("and the number is less than or equal to 60.")

    else:
        print("and it is greater than 60.")

else:
    print("The number is odd ")

    if num <= 60:
        print ("and it is less than or equal to 60.")

    else:
        print ("and it is greater than 60.")    

#date and time

import datetime

dateandtime = datetime.datetime.now()
print(dateandtime)

#calendar

import calendar

calendar1 = calendar.calendar(2016)
print(calendar1)

