# -*- coding: utf-8 -*-

def fibonacci(n):
    print("Suite de Fibonacci : ")
    a,b = 1,1
    resultat = []
    for i in range(n-1):
        a,b = b,a+b
        resultat.append(str(a))
    print(",".join(resultat))

def fibonacci_star(n):
    print("Suite de Fibonacci - version star")
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
        print(a * "*")

if __name__ == '__main__':
    fibonacci(10)
    print("")
    fibonacci_star(10)
