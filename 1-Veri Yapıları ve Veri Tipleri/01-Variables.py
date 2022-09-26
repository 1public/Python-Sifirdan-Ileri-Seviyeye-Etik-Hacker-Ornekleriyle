from os import R_OK


print(5+6)
print(5-6)
print(5*6)
print(5/6)
print(2**3)
print(11 % 2)

# Integer

print(3+3)

# Float

print(0.4 * 3.0)

# Variables

x = 3
y = 5

print(x+y)
print(x**y)

x = 5

print(x+y)

# Yarı Çap Hesaplama
# input ile kullanıcıdan istenen veri metinsel ifadedir, "int()" yapısını kullanarak tip dönüşümü yaptık

r_str = input("r: ")
print(type(r_str))

r_int = int(r_str)
print(type(r_int))

print(r_int*2*3.14)
