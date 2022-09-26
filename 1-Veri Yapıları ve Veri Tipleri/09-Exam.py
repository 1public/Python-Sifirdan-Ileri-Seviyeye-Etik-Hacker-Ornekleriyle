
# String

# 1) Aşağıdaki String'in 5. harfini my_letter isimli bir değişkene atayınız.
from tkinter import Listbox


my_string = "James Hetfield"

# Cevap 1)
my_letter = my_string[4]
print("1. Soru: " + my_letter)


# Aşağıdaki String'in 5. ve 8. karakteri arasındaki tüm harflerini yazdırınız (5 ve 8 dahil)
my_new_string = "QuentinTarantino"

# Cevap 2)
# tinT
# 4. index, 5 karakter ; 8. index 9 karakter
print("2. Soru: " + my_new_string[4:8])

# Aşağıdaki String'i kod ile tersten yazın
my_last_string = "Afyonkarahisarlılaştıramadıklarımızdanmısınız"
# Cevap 3)
print("3. Soru: " + my_last_string[::-1])

#Integer & Float

# 1) Aşağıdaki işlemin sonucu hangi veri tipinde olacaktır?
sonuc = 3 + 10.2 + 50
# Cevap 1)
print(type(sonuc))
# float

# 2) Aşağıdaki işlemin sonucu kaçtır?
cevap = 5 + 8 * 12
# Cevap 2)
print(cevap)

#List & Dictionary & Set

# 1) Bu listeyi 3 farklı yoldan oluşturunuz: [1,2,"a"]
# Cevap 1.a)
list_a = [1, 2, "a"]
print(list_a)

# Cevap 1.b)
list_b = []
list_b.append(1)
list_b.append(2)
list_b.append("a")
print(list_b)

# Cevap 1.c)
list_c = list()
list_c = [1, 2, "a"]
print(list_c)

# 2) Aşağıdaki "a"'yı tek satırda alınız:
my_list = [1, 4, [2, 3, "a"]]
# Cevap 2)
print(my_list[2][2])

# 3) Aşağıdaki "b"'yi tek satırda alınız:
my_dictionary = {"k1": 2, "kk": [4, {"kkkk": "b"}]}
# Cevap 3)
print(my_dictionary["kk"][1]["kkkk"])

# 4) Aşağıdaki liste set'e çevirilince hangi değerler içinde kalacaktır?
my_list_to_be_set = [11, 12, 22, 33, 11, 22, 45, 32, 21, 22, 33, 45]
# Cevap 4)
my_list_to_be_set = set(my_list_to_be_set)
print(my_list_to_be_set)

# Boolean

# 1) Aşağıdaki ifadenin sonucu ne olacaktır?
x = 40 * 5 + 3
y = 208 - 2 * 4
x > y
# Cevap 1)
print(x, y)
print(x > y)  # true

# 2) Aşağıdaki ifadenin sonucu ne olacaktır?
a = 40 * (4 - 2)
b = 80 - 2 * -5
a > b
# Cevap 2)
print(a, b)
print(a > b)  # false
