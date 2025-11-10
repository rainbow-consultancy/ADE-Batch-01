# string formatters

# for i in range(1, 11):
#     print("2 *", i, "=", 2*i)

# 1. .format()
# 2. f""

# for i in range(1, 11):
#     print("2 * {0} = {1}".format(i, 2*i))
    
# for i in range(1, 11):
#     print("2 * {iter} = {product}".format(iter=i, product=2*i))

# for i in range(1, 11):
#     result = f"2 * {i} = {2 * i}"
#     print(result)


# --> Life Cycle and Scope of Variables

# 1. Global Variables  --> life cycle is through out your programme runs and scope of the variable universal
# 2. generic variable (class, function) --> life cycle is limited to its class and function, scope is also restricted to its class or function


def add_sum(a, b, c=10):
    result_sum = a + b + c
    return result_sum

def find_sub(a, b, c=10):
    result = a-b-c
    return result

print(add_sum(20, 10))
print(result_sum)