
# Log Output
In a test with 10 items and a max capacity of 50:

Greed Value to Weight Ratio produced a bag with 130 value and 46 weight in 0.0 seconds.
Greed Maximum Value produced a bag with 139 value and 46 weight in 0.0 seconds.
Greed Minimum Weight produced a bag with 130 value and 46 weight in 0.0 seconds.

Dynamic Programming produced a bag with 139 value and 46 weight in 0.0 seconds.


--------------------------------------------------------------------------------
In a test with 50 items and a max capacity of 100:

Greed Value to Weight Ratio produced a bag with 1122 value and 98 weight in 0.0 seconds.
Greed Maximum Value produced a bag with 971 value and 100 weight in 0.0 seconds.
Greed Minimum Weight produced a bag with 993 value and 90 weight in 0.0 seconds.

Dynamic Programming produced a bag with 1122 value and 98 weight in 0.0010035037994384766 seconds.


--------------------------------------------------------------------------------
In a test with 100 items and a max capacity of 200:

Greed Value to Weight Ratio produced a bag with 1499 value and 197 weight in 0.0 seconds.
Greed Maximum Value produced a bag with 756 value and 200 weight in 0.0 seconds.
Greed Minimum Weight produced a bag with 1365 value and 197 weight in 0.0 seconds.

Dynamic Programming produced a bag with 1499 value and 197 weight in 0.003010272979736328 seconds.


--------------------------------------------------------------------------------


# The 1/0 Knapsack Problem
The 1/0 Knapsack problem is a problem in which you have a bad that can only hold items up to a certain weight. You must find the most optimal combination of items where the knapsack contains the highest possible value of the items inside.

# Strengths and Weaknesses
The greedy algorithms are much faster than dynamic programming, but don't always get the best solution. On the other hand, dynamic programming is guaranteed to find the optimal solution. Dynamic programming is a bit slower, but still fast.  
I implemented three greedy algorithms: Value and Weight Ratio, Max Value, and Minumum Weight. Out of the three value to weight ratio tended to be the best. The other two would often have results far worse than it.  

# Summary
In situations where the optimal solution is necessary, one should do dynamic programming. If speed is more important, I would still use dynamic programming unless the size of the problem is very large. Then I would use the value-to-weight ratio greed algorithm.