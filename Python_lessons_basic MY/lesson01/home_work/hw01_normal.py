 
__author__ = 'niv'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

num = list(input())
x = int(0)
max1 = int(0)

while x < len(num):
    if num[x] >= str(max1):
        max1 = num[x]
        x += 1
    else:
        x += 1
        continue
   
print('ВЫВОД: ', str(max1))






# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input('Введите число а:'))
b = int(input('Введите число b:'))
a, b = b, a
print(a, b)



# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('ax² + bx + c = 0')
a = int(input('Введите число а:'))
b = int(input('Введите число b:'))
c = int(input('Введите число с:'))
import math
d = b ** 2 - 4 * a * c

if d < 0:
	print('Решения нету')
elif d == 0:
	print('x1, x2 =', -b / 2 * a)
else:
	print('x1 = ', -b + math.sqrt(d)) / 2 * a)
	print('x1 = ', -b - math.sqrt(d)) / 2 * a)
