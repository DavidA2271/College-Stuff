# Foreword
I couldn't get deleting to work with the red-black tree. The rotating thing kind of confuses me a little and I spent a lot of time trying to get it to work, but I couldn't figure it out, so I gave up.

# Results
I ran tests with both algorithms with random arrays of sizes 1000, 10000, 100000, and 1000000.
It took 0.0 seconds for the finding and deleting for every size array with both binary trees.

The inserting algorithms took the most time for both trees.
With an array size of 1000, the regular binary tree took 0.0015 seconds. The red black tree took 0.0025 seconds. About double the time.

10000
- BST: 0.022 seconds
- RBT: 0.026 seconds

100000
- BST: 0.28 seconds
- RBT: 0.45 seconds

1000000
- BST: 5.79 seconds
- RBT: 7.62 seconds

The red black tree takes more time to insert, but since it organizes the tree, it is probably faster at searching.

# Analysis
## Inserting
Inserting takes a decent amount more time with a red black tree. Seems like anywhere from 50% to 100% more time. This is probably because it has to inspect the colors of nearby nodes and perform rotations.
## Searching
For searching, I had it search for the last element in the random array. For the red black tree, it probably wouldn't matter which element I chose to search for. But, for the regular binary tree, the last thing added would probably be the furthest element, since it is unbalanced.

Unfortunately any time I tried searching with either the binary search tree or the red black tree, I always came up with 0.0 seconds. I wanted to try with an array bigger than 1 million elements, but inserting took way too long. When I tried 10 million, it took about a minute and a half to insert, but still 0.0 seconds to find a specific element. 
## Deleting
Deleting with the regular binary search tree also always took 0.0 seconds, even when trying with an array with 10 million elements. I got stuck on deleting with the red black tree. I probably made a mistake somewhere, but I've stared at it long enough so I gave up on trying to fix it.

#
I'm sure searching should be faster with a red black tree since it is balanced. I feel like deleting would be slower since it needs to rebalance the tree.