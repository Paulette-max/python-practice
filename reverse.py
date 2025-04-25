def reverse(n):
    word = '' # initialize word
    for i in range(len(n) -1, -1, -1): #goes through each letter
        word += n[i] # stores each letter in reverse
    return word

print(reverse("Hello"))


