#!/usr/bin/env python
# -*- coding: utf-8 -*-
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


print("Bienvenido a Fibonacci")
number = int(raw_input("Ingrese el número de iteraciones"))
result = " n = " + str(number) + " \n"
while number > 0:
    if number == 1:
        result = result +str(fib(number))
    else:
        result = result +str(fib(number)) + " , "
    number = number - 1
print(result)
print("Fin")