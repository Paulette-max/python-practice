def sum(n):
    if n == 0:
        return  0 # base case
    # finding the remainder and adding to sum
    #removing the last digit until it's 0
    return (n % 10) + sum(n // 10)

print(sum(687))
