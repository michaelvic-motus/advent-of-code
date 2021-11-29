# Advent of code: Problem 1
import itertools

# Read data
with open('expense_report.txt', 'r') as file:
    numbers = file.readlines()

# Clean Data
numbers = [float(number.replace('\n', '')) for number in numbers]

# # find 2 numbers
# for num1 in lines:
#     for num2 in lines[1:]:
#         if num1 + num2 == 2020.0:
#             print('The numbers are: ', num1, num2)
#             print('The product is: ', num1*num2)
#             break

# For 3 numbers
for combo in itertools.combinations(numbers, 3):
    if sum(combo) == 2020.0:
        print('Found valid combo:', combo[0], combo[1], combo[2])
        # Find product
        product = 1
        for number in combo:
            product = product*number
        print('The product of the combo is:', product)