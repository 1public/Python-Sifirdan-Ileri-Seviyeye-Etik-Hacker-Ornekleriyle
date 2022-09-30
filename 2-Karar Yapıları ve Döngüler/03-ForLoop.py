my_list = [1, 2, 3, 4, 5]
for number in my_list:
    print(number)

print("---------------------------")

new_number = 1
for item in my_list:
    new_number = new_number * item
    print(new_number)

print("---------------------------")

for number in my_list:
    if number % 2 == 0:
        print(number)

print("---------------------------")

my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item * 3 + 3)

print("---------------------------")

my_new_list = [("a", "b"), ("c", "d"), ("e", "f")]
for element in my_new_list:
    print(element)

for x, y in my_new_list:
    print(x)
    print(y)

print("-------------------------")

my_tuple_list = [(0, 1, 2), (3, 4, 5), (9, 10, 11)]
for (x, y, z) in my_tuple_list:
    print(z)

print("-------------------------")

my_dictionary = {"key1": 100, "key2": 200, "key3": 300}
print(my_dictionary.items())

for key, value in my_dictionary.items():
    print(value)
