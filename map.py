#Without map()

'''
def square(number):
    return number * number

numbers = [1,2,3,4,5]
squared_numbers = []

for number in numbers:
    squared = square(number)
    squared_numbers.append(squared)

print(squared_numbers)
'''

#With map()
def square(number):
    return number * number

numbers = [1,2,3,4,5]
squared_numbers = map(square, numbers);
print(list(squared_numbers))