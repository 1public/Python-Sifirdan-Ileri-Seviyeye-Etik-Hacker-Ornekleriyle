
my_string = "github"

print(my_string[0])
print(my_string[1])

# Immutability

# my_string[0] = "B"
# my_string[1] = "A"

# Mutable

my_list = [1, 2, 3]

print(my_list[0])

print(my_list)

my_list[0] = 5

print(my_list)

my_list.append(7)

print(type(my_list))
print(my_list)

print(my_string.capitalize())

print(my_string)
my_string_capitalize = my_string.capitalize()

print(my_string_capitalize)

print(my_list)
print(my_list.pop())
print(my_list)
my_mixed_list = [1, 2, 3, 4, 5, 6, "a", "metin"]

print(my_mixed_list[-1])

my_list_1 = [5, 6, 7]
my_list_2 = [8, 9, 10]
my_list_3 = my_list_1 + my_list_2
my_list_3.append("-")
print(my_list_3*4)
my_mixed_list.reverse()
print(my_mixed_list)

# Nested List

new_list = [1, 3, 'a']
new_list = [1, 3, 'a', [2, 'v']]
print(new_list[3][1])
print(new_list[:1])
