import json

with open("pi_digits.txt") as file_object:
    contents = file_object.read()
print(contents)

# file_name = "programming.txt"
# with open(file_name, 'w') as file_object:
#     file_object.write("I love programming!")

# json
numbers = [2, 3, 5, 7, 11, 13]
file_name2 = "numbers.json"
with open(file_name2, 'w') as f:
    json.dump(numbers, f)

with open(file_name2) as f:
    numbers = json.load(f)
print(numbers)