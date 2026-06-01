# Write a program that keeps asking the user to enter a password until they
# enter the correct one.

password = 123

check_password = int(input("Enter the password: "))

while (check_password != 123):
    check_password = int(input("Wrong! , Enter again: "))

print('Login Sucessful')
    
