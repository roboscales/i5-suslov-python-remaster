#lab 3 by Suslov
import math
a = 2
b = 3
x = float(input("Введите х: "))
if (x > 0) and (math.cos((a * x)/(2 * b + 1)) <=1 and (math.cos((a * x)/(2 * b + 1)) >= -1)):
    fun = ((2*math.exp(a*x))/(3*(b**2)*(math.pow(a*x, 0.25))))*(((math.cos((a*x)/((2*b)+1))**2)/(1 + ((1)/(math.log(a*x)+b)))))
    print("Значение функции равно: {0:.4}".format(fun))
else:
    print("Значение х не соответствует ОДЗ функции!!!")