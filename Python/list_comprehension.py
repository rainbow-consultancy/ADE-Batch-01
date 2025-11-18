# list comprehension

# 1. build a list with 1 to 10 numbers init
nums = []
for i in range(1, 11):
    nums.append(i)
# print(nums)

nums2 = [i for i in range(1, 11)]
# print(nums2)

odds = []
for i in range(1, 51):
    if i%2 == 1:
        odds.append(i)

# print(odds)

# odds2 = [i for i in range(1, 51) if i%2 == 1]
# print(odds2)   

# odds2 = (i for i in range(1, 51) if i%2 == 1)
# print(list(odds2)) 


# 2. extract names with char length of 5

names = ["John", "Henry", "Kohli", "Rohith", "Dhoni", "Omi"] #--omi

qualified_names = [name for name in names if len(name) == 5]
# print(qualified_names)

qualified_names = [name for name in names if len(name) != 5]
# print(qualified_names)

# 3. extract names with in which it contains 'o' and its count
qualified_names = [name for name in names if 'O' in name.upper()]
print(qualified_names)
print(len(qualified_names))