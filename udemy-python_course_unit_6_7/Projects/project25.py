def reverse_string(input_str):
    return input_str[::-1]
original_string = input(str("Enter a string: "))
reversed_string = reverse_string(original_string)
print(reversed_string)