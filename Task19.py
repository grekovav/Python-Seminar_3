# 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3    Output: [4, 5, 1, 2, 3]

# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на
# K элементов вправо, K – положительное число.
# 1 2 3 4 5 6 7 8 9
# 2

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = int(input("Введите число сдвига: "))
print(a[-k:] + a[:-k])
