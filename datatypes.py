# # DataTypes

# # creating and defining a list
# fruits = ["mango", "apple", "dragonFruit"]

# # add new item to the list
fruits.append("Orange")

# # modify a item in the list like dragonFruit -> Dragon Fruit
fruits[2] = "Dragon Fruit"

fruits2 = ["Banana", "Persimmon"]

# # merge 2 lists into a single list
fruits.extend(fruits2) # --> ["mango", "apple", "dragonFruit", "Banana", "Persimmon"]

# # what if I do append to merge the 2 lists
fruits.append(fruits2) # --> ["mango", "apple", "dragonFruit", ["Banana", "Persimmon"]]

# # how to delete the last item from the list
fruits.pop()

# # how to delete a specific item from the list
fruits.remove("mango")  # --> removes mango from the list

fruits.index("apple") # gives the position of the item in the list -> 1

len(fruits) # --> will gives you the count of no of items in the list


# --------------------------------------------------------

# Tuple

my_tuple = ("mango", "apple", "banana", "mango", "mango")
cnt = my_tuple.count("mango")
print(cnt)

cnt = my_tuple.count("apple")
print(cnt)

print(my_tuple.index("banana"))
m = my_tuple + ("orange", "Jamun")
print(m)


my_tuple.append(20)

my_tuple[5] = "Kiwi"
print(my_tuple)

my_tuple[0] = "watermelon"
print(my_tuple)

# # --- work around to modify a tuple
my_tuple_temp = list(my_tuple)
print(my_tuple_temp)

my_tuple_temp[4] = "watermelon"
print(my_tuple_temp)

my_tuple = tuple(my_tuple_temp)
print(my_tuple)

# ---------------------------------------------
# SET

# --> set is a unordered datatype (which means the order is not guarenteed)
# and also it won't support indexing and additionally set won't carry any duplicate values
my_set = {"mango", "banana", 1, 2, 3, 3, 3, 4, 5, 5, 5}
# print(my_set)

# # add items in to a set
# my_set.add(6)
# print(my_set)

# print(len(my_set))

# my_set.remove("mango")
# print(my_set)
# print(len(my_set))

# my_set[0] = "orange"  not accepted
# print(my_set[0])

# -------------------------------------------

# dictionary

stu_info = {
    "name": "Dileep",
    "age": 24,
    "subjects": ["Kannada", "English", "Telugu"]
}

print(stu_info)

print(type(stu_info))

# print(stu_info[0])

print(stu_info["name"])


print(stu_info["subjects"])

print(stu_info["subjects"][2])

print(stu_info.get("age"))

stu_info["city"] = "Bangalore"
print(stu_info)

stu_info["age"] = 25
print(stu_info)

print(stu_info.keys())
print(stu_info.values())
