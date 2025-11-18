# deep dive into loops

# 1. Print 2 table on the console
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# .
# .
# 2 * 10 = 20

# for i in range(1, 11):
#     print("2 *", i, "=", 2*i)
    # print("3 *", i, "=", 3*i)
    
    
# 2 * 1 = 2
# 3 * 1 = 3
    
# 2. print 4 table on the console

# for i in range(1, 11):
#     print("4 *", i, "=", 4*i)

# 3. print 2-5 tables on to the console

# 2 * 1 = 2
# 2 * 2 = 4

# 3 * 1 = 3
# 3 * 2 = 6

# 4 * 1 = 4
# 4 * 2 = 8

# 5 * 1 = 5
# 5 * 2 = 10

# for i in range(2, 6): # i = 2 
#     for j in range(1, 11): # until range ends J value changes but not i value
#         print(i, "*", j, "=", i*j)
#     print("-------------------------------")

# left pyramid
# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1, 6):
#     print(i * "* ")

# for i in range(6, 0, -1):
#     print(" *" * i)
    
#  * * * * * *
#  * * * * *
#  * * * * 
#  * * *
#  * *
#  *

# for i in range(1, 11):
#     print(" " * (10 - i) + "*" * i)

#      *
#    * *
#  * * *

rows = 5
i = 1

# while i <= rows:
#     print("*" * i)
#     i+=1 # i = i + 1 
    

# 1. break
# 2. continue

# for i in range(1, 11):
#     print(i)
#     break
    # if i == 5:
    #     break

# for i in range(1, 11):
#    if i == 5:
#        continue  # -- skip the value
#    else:
#         print(i)
        
for i in range(1, 11):
#    if i == 5:
    continue  # -- skip the iteration
    print(i)