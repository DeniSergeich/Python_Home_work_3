# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 3
# -> 1

new_list = list(map(int, input("Введите массив через пробел: ").split()))
number = int(input("Введите число: "))
print(len([i for i in new_list if number == i]))