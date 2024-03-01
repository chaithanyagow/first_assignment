# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 14:25:51 2024

@author: chait
"""
"""
1.
a=int(input())
b=int(input())
print(a+b)
"""
"""
2.
a=int(input())
b=int(input())
c=max(a,b)
print(c)
"""
"""
3.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input())
if num < 0:
    print("Factorial not defined")
else:
    result = factorial(num)
    print(result)
"""
"""
4. 
P=int(input())
T=int(input())
R=int(input())
SI=(P*T*R)/100
print(SI)
"""
"""
5. 
P=float(input('enter principal: '))
R=float(input("interest: "))
T=float(input('time: '))
CI=(P*(1+R/100))**T
print(CI)
"""
"""
7.
import math
r=eval(input('enter radius: '))
area= math.pi*(r**2)
print(area)
"""
"""
6.

def armstrong(n):
     numstr = str(n)
     
     digits = len(numstr)
     
     armstrongsum = sum(int(digit)**digits 
for digit in numstr)
    
     return n == armstrongsum

x = int(input("Enter a number: "))
if armstrong(x):
     print(x, "it is armstrong number")
else:
     print(x, "it is not an armstrong number")



8.

x=eval(input("Enter the range"))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

x, y = eval(input("Enter the range (x, y): "))

for n in range(x, y+1):
    if is_prime(n):
        print(n)


9.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

x = int(input("Enter number: "))
if is_prime(x):
    print(x, "is prime")
else:
    print(x, "is not prime")


10.
def fibonacci(n):
    if n <= 0:
        return " enter a positive integer."
    elif n == 1 or n == 2:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input(" value of n: "))
print(fibonacci(n))
"""







