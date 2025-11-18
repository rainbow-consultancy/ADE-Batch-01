# loops in python

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# 1. for loop
# 2. while loop

# for i in range(start, stop, step=1)

# for i in range(1, 11, 3):
#     print(i)

# i = 1
# while i <= 100:
#     print(i)
#     i = i + 1


# strings, lists, set, tuple, dict

name = "python"
# for i in name:
#     print(i)

# fruits = ["apple", "banana", "mango"]
# # for fruit in fruits:
# #     print(fruit)
    
# stu_info = {
#     "name": "Sandeep",
#     "age": 29,
#     "course": "M.sc"
# }

# for key, value in stu_info.items():
#     print(value)
    

name = input("Enter the name: ")
# print(type(name))

# count the noOf vowels in the name variable
# [a, e, i, o, u]
vowels = ['a', 'e', 'i', 'o', 'u']

cnt = 0
special_chars = ['!', '@', '#', '$', '%']

char_cnt = 0
for i in name:
    if i in special_chars:
        char_cnt = char_cnt+1
        
# conditional operators
if name.isnumeric():
    print("You have entered a numeric value. Pls enter a string!")
    
elif char_cnt > 0:
    print("Entered string contains special chars!!")

else:
    for ch in name.lower():
        if ch in vowels:
            cnt = cnt + 1
    print(cnt)
        


# if condition:
#     code
# elif condition2:
#     code
# elif condition3:
#     code
# else:
#     code