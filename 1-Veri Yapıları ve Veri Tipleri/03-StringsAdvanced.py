# stringleri dizi gibi kullanabiliriz
my_string = "hello world"

print(my_string)

print(my_string[1])
print(my_string[-1])

# Slicing: Dilimleme

my_string2 = "1234567890"

print(my_string2[0])
print(my_string2[2:])
print(my_string2[4:])

# Stopping Index
print(my_string2[:2])
print(my_string2[2:4])
print(my_string2[-3:-1])

# Step Size
print(my_string2[::3])
print(my_string2[1:4:2])
print(my_string2[::-1])

# String Methods
# Oluşturduğumuz değişkenlerin methotlarını kullanabiliriz
my_name = "github"
print(my_name.capitalize())
my_name_captialize = my_name.capitalize()

print(my_name_captialize)

my_name2 = "git hub"

print(my_name2.split())

my_name2_split = my_name2.split()

print(my_name2_split)
print(my_name2_split[1])

print(my_name.upper())

print(my_name*3)

full_name = my_name + " " + my_name2

print(full_name)
