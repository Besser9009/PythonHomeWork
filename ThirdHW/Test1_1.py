# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random
A = []
N = int(input("Введите количество элемнтов массива: "))
X = int(input("Введите проверяемое число: "))
for i in range(N):
    n = random.randint(0, 10)
    A.append(n)
print(N)
print(A)
count = 0
for i in range(N):
    if A[i] == X:
        count += 1
print(X)
print(f'-> {count}')