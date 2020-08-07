#Without zip
'''
...
even_numbers = [2,4]
even_numbers_squared = [4, 8]
combined = []
even_numbers_index = 0
for number in even_numbers:
    squared = even_numbers_squared[even_numbers_index]
    squared_tuple = (number, squared)
    combined.append(squared_tuple)

print(combined)
'''

#With zip
...
even_numbers = [2,4]
even_numbers_squared = [4, 8]
zipped_result = zip(even_numbers, even_numbers_squared)

print(list(zipped_result))