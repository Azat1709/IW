import math
x = float(input("Введите действительное число x: "))
n = int(input("Введите натуральное число n: "))
result = 0
for i in range(1, n + 1):
    result += (x ** i) / math.factorial(i)
print('Результат выражения x^1/1! + x^2/2! + ... + x^n/n! равен:' ,result)


