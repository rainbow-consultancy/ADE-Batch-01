# # python functions | method

# # casing

# # 1. Camel Casing --> camelCasingFormat

# # ex:- findSum

# # 2. Pascal Casing --> PascalCasingFormat

# # ex:- FindSum

# # 3. Snake Casing --> snake_casing

# # ex:- find_sum

# def find_sum(a: int, b: int) -> int:
#     return a + b

# # print(find_sum())

# def calculator(operation: int, a: int, b: int) -> int:
#     if operation == 1:
#         return a + b
#     elif operation == 2:
#         if a < b:
#             return "Error: a value should be greater then b value"
#         else:
#             return a - b
#     elif operation == 3:
#         return a * b
#     else:
#         return "Operation Invalid"
    

# # print(calculator(operation=2, a=100, b=200))
# # print(calculator(operation=2, a=200, b=100))
# # print(calculator(operation=1, a=200, b=100))
# # print(calculator(operation=0, a=200, b=100))
    

# # def greet(name: str = "Unknow") -> str:
# #     return "Good Evening " + name

# # print(greet("Sandeep"))
# # print(greet("Rohith"))
# # print(greet())

# def greet(name: str = "Unknow") -> str:
#     return "Good Evening " + name

# # print(greet())

# # range()

# result = 10

# def add_sum(a, b, c=10):
#     result_sum = a+b+c
#     return result_sum

# def find_sub(a, b, c=10):
#     result = a-b-c
#     return result

# # print(add_sum(10, 30, 40))

# def add_sum(a, b, c):
#     return a+b+c

# print(add_sum(10, 30, 40))

# print(add_sum(c=10, b=30, a=40))

# even = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         even.append(i)
# print(even)


# list comprehension

even = [i for i in range(1, 11) if i%2==0]
print(even)