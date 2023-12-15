x = float(input("Введите действительное число x: "))
n = int(input("Введите натуральное число n: "))
result = 0
current_denominator = 1
for i in range(n + 1):
    current_denominator *= (x + i)
    result += 1 / current_denominator
print('Результат выражения равен: ',result)
