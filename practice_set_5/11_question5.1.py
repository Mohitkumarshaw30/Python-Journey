# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"}
# and:
# Print the value of "name" .
# Change "grade" to "A+" .
# Add a new key "city" with value "Delhi" .

student = {"name":"John" , "age":20 , "grade":"A"}

print(student)

print(student["name"])

student["grade"] = "A+"
print(student["grade"])

student.update({
    "city":"Delhi"
})

print(student)
