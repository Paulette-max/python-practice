def elements(numbers):
    total = 0  # used a loop to go through each element in the list
    for i in numbers:
        total+= i
    return  total

numbers = [1, 2, 3, 4, 5]
sum_elements = elements(numbers)
print("Total:", sum_elements)