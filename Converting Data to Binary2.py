def string_to_binary(s):
    return ' '.join(format(ord(char), '08b') for char in s)

text = "Hello"
binary_representation = string_to_binary(text)
print(f"Binary representation of '{text}' is {binary_representation}")

