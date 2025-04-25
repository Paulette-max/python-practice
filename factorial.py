def factorial(n):
    result = 1 #initialize as 1 because factorail of 0 is 1
    for i in range(1, n + 1):
        result *= i #looping through and multiplying until target number is reached
    return result

print(factorial(6))


