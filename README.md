# python-practice
Name: Paulette Mbaika
Admission No: 190016

1. Sum all elements in a list.
   I knew I needed to go through each element in the list so I knew I needed a for loop, so I started with that.
   I intialized the total variable and created the for loop which iterated through the list and added them together.
   I then gave the function a value and printed it.
   
2. Check if a number is even or odd.
   I defined the function first and made an if-else loop.
   My logic was if something is divisible by 2, it's even, if not it's odd.
   I used the modulo operator to see if the number is divisible by 2.
   I also decided to have an input function for some fun.

3. Compute factorial using a loop.
   My first thought was to use an if-else statement, but I realized it would be too similar to question 5.
   Instead, I used a for loop with the range function to go through each number from 1 to n and multiply i by the result   
   variable.

4. Reverse a string (without using [::-1] or built-in methods).
   I knew I needed to use the len function to go through each letter, but I couldn't think of how, so I used Google
   which helped me with the for loop I used.
   I intialized the word variable so I would have something to store the result in and then made the for loop with len(word) 
   -1 which tells the loop the last index, -1 to stop before 0, and -1 to move backwards with each letter.
   I then added each character backwards and printed it.

5. Factorial (Recursive)
   I used an if-else statement and intialized n to start at 1 and then made the return statement a simple formula to compute
   the factorial.
   
6. Sum of Digits of a Number
   This was a little hard to figure out so I again turned to Google and found a Reddit post which advised on using the modulo 
   and floor division operators. After figuring out how it worked on my calculator, I wrote my code.
   I started the same way as the factorial function but started with 0 instead as the base case.
   Then the return statement had a modulo operator that extracted the last digit of the number and then added
   the sum and what was left after removing the last digit.

   
