import math
n = int(input("Введите натуральное число n: "))
sum_result = 0
current_sin_sum = 0
for i in range(1, n + 1):
    current_sin_sum += math.sin(i)
    sum_result += 1 / current_sin_sum
print(' сумма равна: ',sum_result)
