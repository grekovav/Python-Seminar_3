# 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 5 3 4 2
# 3
# -> 1

n = int(input('Введите количество элементов массива: '))
numbers = [int(i) for i in input('Введите значения элементов через пробел: ').split()]
if len(numbers) != n or n == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    x = int(input('Введите искомое число X, количество вхождений которого нужно подсчитать: '))
    print(f'Число {x} в массиве встречается {numbers.count(x)} раз')
