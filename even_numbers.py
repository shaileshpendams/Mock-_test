def only_the_even(numbers):
    return [num for num in numbers if num % 2 == 0]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# input = input('list')
output_list = only_the_even(input_list)
print(output_list)
