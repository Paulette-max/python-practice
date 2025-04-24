number = int(input("Enter a number: ")) # input
def check(number):
    if number % 2 == 0: #if the number is divisible by 2, it is even
        return "Even"
    else: # if not, it is odd
        return "Odd"


even_odd = check(number)
print(even_odd)

