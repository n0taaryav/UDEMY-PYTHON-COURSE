def count_words(input_str):
    words = input_str.split()
    return len(words)

original_string =input(str("Enter a string: "))
word_count = count_words(original_string)
print(word_count)
