input_string = input("Enter a string: ")
transformed_string = ''

for index, char in enumerate(input_string):
    if index % 2 == 0: 
        transformed_string += char.lower()
    else: 
        transformed_string += char.upper()

print("Transformed string:", transformed_string)
