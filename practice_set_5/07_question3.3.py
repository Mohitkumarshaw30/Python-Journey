# Convert the tuple to a list, change its first element to 50 , and convert it back
# to a tuple.

tuple_num = (1,2,3,4,5)
print(tuple_num)

# list = [i for i in (tuple)]

list_num = list(tuple_num)
print(list_num)

list_num.pop(0)
list_num.insert(0,50)
print(list_num)

num = tuple(list_num)
print(num)
