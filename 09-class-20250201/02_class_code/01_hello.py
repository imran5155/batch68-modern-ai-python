""" This is a simple hello world program """

def add (first_num:int, second_num:int) -> int:
    """
    Takes two numbers and return the sum of them

    Args:
        first_num: int
        second_num: int

    Returns:
        int: sum of first_num and second num

    """
    return first_num + second_num



result = add(1, 2)



# List Comprenhension

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # List of squares of nums

# square = []

# for num in nums:
#     square.append(num ** 2)

# print(square)


# squares = [num **2 for num in nums]

# print("List comprehension", squares)

#  ==================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List of squares of nums

square = []

for num in nums:
    if num >= 5:
     square.append(num ** 2)

print(square)


squares = [num **2 for num in nums if num >= 5]

print("List comprehension", squares)

