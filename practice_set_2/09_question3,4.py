# Print the following pattern using a for loop:

# *
# **
# ***
# ****

for i in range(1,5):
    for j in range(0,i):
        print('*',end="")
    print("")


# or

'''
Print the following pattern
*
**
***
****
'''

for i in range(1, 5):
    print("*"*i)