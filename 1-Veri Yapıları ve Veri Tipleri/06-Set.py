

my_list = [1, 2, 3, 1]
print(my_list)
print(type(my_list))

# Casting

my_set = set(my_list)
print(my_set)

# süslü parantez içinde liste oluşturursak aynı değeri iki kez atayamyız
my_set_2 = {2, 2, 3, 2}
print(my_set_2)

print(type(my_set_2))

my_set_3 = {"a", "b", "a"}
print(my_set_3)


print("------------")  # list, dictionary, set kullanmı
liste = [1, 2, 3]
print(type(liste))

sozluk = {"key1": 100, "key2": 200}
print(type(sozluk))

set1 = {1, 2, 3}
print(type(set))
print("------------")

my_set_4 = {}
print(my_set_4)
print(type(my_set_4))

my = set()
print(type(my))
print(my)
my.add(1)
my.add(2)
my.add(3)
print(my)
my.add(1)  # set olduğu için aynı değeri iki defa kullanamazsın
print(my)
print(type(my))

my2 = dict()
print(my2)
print(type(my2))

my2["merhaba"] = 10

print(my2["merhaba"])

my_list_10 = list()

print(type(my_list_10))

print(my_list_10)
