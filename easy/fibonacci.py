
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    n2, n1 = 0, 1

    for _ in range(2, n+1):
        n1, n2 = n2 + n1, n1

    return n1

print(fibonacci(20))
