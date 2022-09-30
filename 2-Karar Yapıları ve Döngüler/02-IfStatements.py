if 2 > 1:
    print("Github")
    print("12345")
x = 3
y = 10

if x > y:
    print("x is greater")
elif x == y:
    print("x is y")
else:
    print("y is greater")


my_superhero = input("Superhero: ")
if my_superhero == "Batman":
    print("Batmaaan")
elif my_superhero == "Superman":
    print("Supermaan")
elif my_superhero == "Ironman":
    print("Ironmaan")
else:
    print(":(")

a = 10
b = 25
c = 20

if a > b or b < c:
    print("superman")
elif a < b and b > c:
    print("batman")
else:
    print("aquaman")

isDead = False

if isDead == True:
    print("character is dead")
else:
    print("character is not dead")

if isDead:
    print("character is dead")
else:
    print("character is not dead")
if not isDead:
    print("character is not dead")

# -----------pratik-------------

my_string = "Hello World"
if my_string == "Hello World":
    print("equal")

if "Hello" in my_string:
    print("true")
else:
    print("false")

my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("true")
else:
    print("false")

my_dictionary = {"k1": 100, "k2": 200, "k3": 300}

if 2010 in my_dictionary.values():
    print("true")
else:
    print("false")
