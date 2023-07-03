def only_the_even(numbers):
    return [num for num in numbers if num % 2 == 0]

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# input = input('list')
output = only_the_even(input)
print(output)
