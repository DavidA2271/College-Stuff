# Analysis
The time complexity of my algorithm is O(n).  
First I loop through all vertices to count their edges, O(n).  
Next is a while True loop which is constant.  
Inside of the while loop, I iterate over every adjacent node connected to the current node on the path. I'm not certain if this affects the time-complexity of the algorithm. However I do this process for evry single node on the path, which is n if a Hamiltonian path is made. SO I think this is linear time as well.  
I also always reverse the path once upon hitting a dead end, so I can check nodes connected to the "start" of the path. This is also linear time.

# Approach
At first I had the obvious idea of just checking every permutation of paths. But I like making things more efficient so I spent a while thinking of other ways to do it.  

After looking at and drawing a bunch of graphs, I realized the Hamiltonian Path is just a line. I had the idea that if I could somehow flatten the graph into a line, I could make a Hamiltonian Path.  

It's kind of hard to explain with no visuals.  

After looking at more graphs, I realized that the "most crucial" portion of making a path is to focus on nodes with less edges. If a node only has one edge, that edge must be used in the path.  

Using this idea, I made an algorithm that starts at the node with the least edges. I then selected the adjacent node with the least amount of edges as the next node to visit.  

The resulting algorithm worked very well. I tested it out with on about  hundred generated graphs and I notice any problems.  
I'm not sure if this is a foolproof approach, but it definitely works very well.
