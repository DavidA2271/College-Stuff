# Traveling Salesman Problem
The traveling salesman problem is a famous computation problem due to it's computational difficulty. In the problem there an arbitrary amount of cities an arbitrary distance apart. You must develop an algorithm that finds the shortest path that visits all of these cities and returns to the starting city. However, there does not exist any polynomial time solution to the traveling salesman problem, since all solutions must explore a number of permutations of the cities which takes exponential time.

# Brute Force
In the brute force method I explored all possible permutations possible paths to find the definitively shortest path. I used python's itertools library to generate permutations of indexes based on how many nodes or 'cities' the graph had in it. This part of the algorithm has the worst time complexity in the whole algorithm. It has an exponential time complexity. This can't really be avoided when you have to calculate every permutation. Because of this, the brute force method scales very badly with larger sized problems.

# Ant Colony Optimization
I chose to use the ant colony optimization technique. This technique has two special features to help it find an optimal path. It uses inverse probability for the shortest paths between cities, and a pheromone matrix.  
The inverse probability works similar to the nearest neighbor algorithm. The difference is that inverse probability introduces rng to which path is taken, with a bias to shorter paths. This helps the algorithm broaden its search range as it is not constricted to always going the shortest path at the moment.  
The second feature is the pheromone matrix. It is a matrix of multipliers that increases the chance that a certain path be taken. After tha algorithm finishes an iteration, it updates this matrix with the shortest found path so it is more likely to be chosen on subsequent iterations.  
The reason I chose this algorithm was very simple. It made the most sense to me when looking at all of the other options, so I thought I would have the easiest time implementing this one.

# Results
Due to its nature, the brute force solution takes the most time, but always gives the optimal solution. During testing, the ant colony optimization usually came close to the brute force solution, but rarely had the exact same result. Of course, it was never a better result than brute force.  
When testing both algorithms on the same graph of 8 cities, it took the brute force algorithm about 60 seconds to complete each time. However, it only took the ant colony algorithm about a tenth of a second on average.
Others result was never better than brute force.  
When testing the brute force method with more than 8 cities, it took much longer. With 10 nodes, I had the program running for 5 minutes and it still did not complete, so I stopped it.  
On the other hand, I had the ant colony optimization method run through 100 cities with 50 ants for 100 iterations and it took only 15 seconds. Whether or not the solution it came up with was the most optimal, I'm not sure, but it is very fast.