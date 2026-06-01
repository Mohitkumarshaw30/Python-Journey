# Create a program that checks if a person is eligible to vote (age >= 18).

age = int(input("Enter your age: "))

if(age>=18):
    print("You can vote")
elif(age>0 and age<18):
    print("You can not vote")
else:
    print("Please enter a valid age")
