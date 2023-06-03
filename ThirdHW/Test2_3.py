# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random
A = []
N = int(input("Введите количество элемнтов массива: "))
X = int(input("Введите искомый элемент: "))
for i in range(N):
    n = random.randint(1, 10)
    A.append(n)
print(N)
print(A)
number = -11
i = 0
while i < N:
    if A[i] == X:
        number = A[i]
    elif (X - A[i]) < 0 or (X - number) < 0:
        if (X - A[i]) < 0 and (X - number) > 0:
            num1 = -1 * (X - A[i])
            if num1 < (X - number):
                number = A[i]
        elif (X - number) < 0 and (X - A[i]) > 0:
            num2 = -1 * (X - number)
            if num1 < (X - number):
                number = A[i]
        elif (X - A[i]) < 0 and (X - number) < 0:
            num1 = -1 * (X - A[i])
            num2 = -1 * (X - number)
            if num1 < num2:
                number = A[i]
    else:
        if (X - A[i]) < (X - number):
            number = A[i]
    i += 1
print(X)
print(f'-> {number}')