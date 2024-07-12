import math

def composite_trapezoidal(f,a,b,n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    for i in range(1,n):
        result += f(a + (i*h))
    return result*h

def f(x):
    return math.e**(-x**2)

answer = composite_trapezoidal(f,0,1,10)
print(answer)



