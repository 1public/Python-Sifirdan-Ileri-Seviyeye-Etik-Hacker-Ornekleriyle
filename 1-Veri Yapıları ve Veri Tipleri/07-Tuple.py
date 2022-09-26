# Tuple de bir listedir,fakat içine atanan bir değer bir daha değiştirilemez
my_tuple = ("a", 1, "c")
print(my_tuple[0])
# Immutable - 5 satır hata verecektir
# my_tuple[0] = "u"
my_tuple_2 = (1, 1, 1, 0, "a")
print(my_tuple_2.count(1))  # kaç tane oluğu bilgisi
print(my_tuple_2.index("a"))
