# Create a dictionary of three friends and their phone numbers. Use:
# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them

name_phone = {"Rajendra":"1122332233" , 
              "Gajanana":"0000000000" ,
              "Rajnikant":"1111133333"}

print(name_phone.keys())
print(name_phone.values())

for name,phone in name_phone.items():
    print(name,":",phone)