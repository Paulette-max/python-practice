def fact(n):
    if n == 1: # starting at 1 because factorial of 0 is 1
        return 1
    return n * fact(n - 1) # subtracting from n and then multiplying

print(fact(5))
