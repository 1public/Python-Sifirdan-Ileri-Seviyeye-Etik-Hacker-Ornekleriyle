my_dictionary = {"key": "value"}
my_list = ["key"]

my_fitness_dictionary = {"run": "100", "swim": "200"}
print(my_fitness_dictionary["run"])
print(my_fitness_dictionary["swim"])

my_dictionary_2 = {"key1": 1, "key2": 2, "key3": 3, "key4": "apple"}
print(my_dictionary_2["key2"])

my_dictionary_3 = {10: 20, 30: 40}
print(my_dictionary_3[30])

# sözlük içerisinde liste oluşurulabilir
my_dictionary_4 = {"key1": 1, "key2": [10, 20, 30], "key3": {"a": 5}}

print(my_dictionary_4.keys())
print(my_dictionary_4.values())

print(my_dictionary_4["key2"][2])

print(my_dictionary_4["key3"]["a"])

my_dictionary_5 = {"key1": 10, "key2": 20}
print(my_dictionary_5)
my_dictionary_5["key2"] = 77
print(my_dictionary_5)
my_dictionary_5["key3"] = 17
print(my_dictionary_5)
