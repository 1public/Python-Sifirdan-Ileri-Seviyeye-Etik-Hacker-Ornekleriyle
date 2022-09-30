my_list = [10, 20, 30, 40, 50]

for number in my_list:
    print(number * 5)

print("----------------")

for number in my_list:
    if number == 30:
        break
    print(number * 5)

print("----------------")

for number in my_list:
    if number == 30:
        continue
    print(number * 5)

print("----------------")


for no in my_list:
    pass
