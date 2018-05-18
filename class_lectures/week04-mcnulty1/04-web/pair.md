#### Pair Problem

This is a classic problem. This particular wording is varition on the text from [Cracking the Coding Interview](http://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/098478280X) (question 9.8):

**For questions 1, 2 and 3, you don't need recursion. For question 4, try to see if you can do it without recursion. Then do question 4 with recursion.**

1) Given enough pennies (1 cent) and nickels (5 cents), how many ways can you make change for a given amount of cents? Your function will be def ways(cents).

    Example: ways(12) will return 3. 
    (Because there are three ways: 2 nickels and 2 pennies, 1 nickels and 7 pennies, 12 pennies.)

2) Given enough pennies (1 cent), nickels (5 cents) and dimes (10 cents), how many ways can you make change?

3) Given enough pennies (1 cent), nickels (5 cents), dimes (10 cents) and quarters (25 cents), how many ways can you make change?

4) Given an arbitrary set of coin types, how many ways can you make change? Your function will now look like this:

    def ways(cents,coinTypes):
  
  And you will call it this way:
  
    ways(100,[25, 10, 5, 1])
    242
