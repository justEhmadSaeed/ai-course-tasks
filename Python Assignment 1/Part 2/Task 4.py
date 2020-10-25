# Find the series of Fibonacci numbers using lambda function.


from functools import reduce

def Fibonacci(n):
    series = [0, 1]
    for _ in range(2, n):
        series.append(reduce(lambda a, b: a + b, series[-2:]),)
    return series


fibNum = int(input("Enter a number: "))
print("Fibonacci Sequence" , Fibonacci(fibNum))