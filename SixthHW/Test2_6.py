#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
array = []
for i in range(25):
    elem_array = random.randint(0, 100)
    array.append(elem_array)
min = int(input("Введите минимальный порог поиска: "))
max = int(input("Введите максимальный порог поиска: "))
print(array)
for i in range(25):
    if min <= array[i] <= max:
        print(f"{array[i]}: {i}")