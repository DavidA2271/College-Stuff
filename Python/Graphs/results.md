# Foreword
Unfortunately I only completed the BFS and DFS. I couldn't quite figure out Dijkstra and am running out of time to submit.

# Testing
I tested both BFS and DFS. In the few examples I did, both algoithms worked very fast. They took about 0.0005 seconds or so each. It looked like BFS was slightly faster number wise though.  
I was unable to test with 500 nodes and 1000 edges. I used recursion to implement both methods and I hit python's recursion limit.

# Analysis
The time complexity of DFS the way I implemented it is O(n^2). I use recursion to loop over all nodes and use another loop inside to add all connected edges to a list.  
The time complexity of BFS is the same. I implemented both methods in a very similar fashion. I used recursion for both and looped over connected edges.  
There was only one line of code that was different in how I implemented both algorithms, so it makes sense they both have similar time complexity. I added all connected edges to a list. In DFS I popped the last element and recursed with that, which would take me to the deepest branch first. In BFS I popped the first element in the list which allowed for breadth first instead.