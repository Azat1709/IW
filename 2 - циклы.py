x = float(input("Введите действительное число x: "))
n = int(input("Введите натуральное число n: "))
result = 1

for i in range(n + 1):
    result *= (x - i * n)
print('Результат выражения x(x-n)(x-2n)(x-3n)...(x-n²) равен:',result)
