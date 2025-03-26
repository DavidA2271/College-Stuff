# Analysis
I can't say it is the fastest program, but it works well. It evaluates every blank cell for possible values that can be put in it and chooses a random one. This means that for every cell, it evaluates 27 other cells (9 in each row, column, and box) to decide what can be put in it.  

While testing it only solved a sudoku once. Most of the time it had less than 10 errors though. Errors are calculated by if there are two of the same number in the same row, column, or box. At first I had it iterate 100 times, but I ended up increasing it to 10,000. It only took my computer about 10 seconds for each run, and the results were much better.

# Approach
This was probably the hardest question for me on the exam. I did all of the question in order except this one. I tend to prefer algorithms that give absolute solutions rather than heuristics, so this one was a little confusing for me.  

Since the goal was a heurstic solution, first I had to decide on the heuristic value. The main rule of sudoku is the nonrepeating 1-9 in every row, column, and box, so I chose that. I narrowed down the choices for each cell based on values in filled cells to reduce errors. Then I just compared the error between iterations and kept the one with the lowest error.  