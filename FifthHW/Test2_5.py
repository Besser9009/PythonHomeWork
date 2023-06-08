# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 
import module
def Start():
    a = int(input("Введите число a: "))
    b = int(input("Введите степень, в которою будет возведено число a: "))
    if a > b > 0:
        sum = module.sumnumber_A(a, b)
    elif b > a > 0:
        sum = module.sumnumber_B(a, b)
    elif a < b and a < 0:
        sum = module.sumnumber_minA(a, b)
    elif b < a and b < 0:
        sum = module.sumnumber_minB(a, b)
    print(f"{a} + {b} == {sum}")
Start()