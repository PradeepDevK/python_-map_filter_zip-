#Without filter
'''
def even(number):
    if (number % 2) == 0:
        return True
    return  False

numbers = [1,2,3,4,5]

even_numbers = []
for number in numbers:
    if even(number):
        even_numbers.append(number)

print(even_numbers)
'''

#With filter
def even(number):
    if (number % 2) == 0:
        return True
    return  False

numbers = [1,2,3,4,5]
even_numbers = filter(even, numbers)

print(list(even_numbers))