# Algorithm Analysis
1. The worst-case time complexity would be O(n^2*log(n)). The algorithm has 3 nested loops.  
<br>
The first loops over the size of the array, so that's already linear time complexity.  
<br>
The second loop is also dependent on the size of the array, so linear as well. While it will loop less times than the size of the array, that does not change the fact that it is dependent on the size of the given array. This makes at least O(n^2) time.  
<br>
The third loop is not linear time. The variable k is always set to 1 and then multiplied by 2 until k is greater than the size of the array. Meaning the multiplication operation will be performed 2^x times where x equals log(n) where the log base is 2. So the third loop has a time-complexity of log(n).  
<br>

2. The worst-case time-complexity would be O(n^2) since both loops are dependent on the size of the input array. The best-case scenario would be if the input array always had a size of 1. In which the time-complexity of the algorithm would be O(1) as each loop would only loop a single time.  
<br>

3. In order to find the kth smallest element in an array, you would need to sort the enttire array first. This is because, for example, to find the fifth smallest element, you would need to find the first, second, third, and fourth smallest as well.  
<br>
The best algorithm to use in this case would be an insertion sort. In Assignment 2, we had to compare various sorting methods, and I found that insertion sorts were the fastest out of selection, bubble, insertion, and radix sort.  
<br>
In the worst-case scenario, the list would be in greatest to least order, giving insertion sort a time-complexity of O(n^2). If the array were already sorted, the time-complexity would be O(n).  
<br>

4. Time-complexity is a measure of how long an algorithm would take for a CPU to process. Space-complexity is a measure of how much additional space will be taken in a computers memory.  
<br>
An example of low time-complexity, but high space-complexity would be an algorithm that takes no arguments and creates an array with a million elements. Time-complexity is constant, since it will always make the array with a million elements independent of whatever input you give it. Space-complexity is high, since it makes a really big array.  
<br>
An example of high time-complexity, but low space-complexity would be an insertion sort. If implemented correctly, an insertion sort will take O(n^2) time in its worst-case scenario. However, it only rearranges elements in the given array, and does not create much additional space.  
<br>

# Data Structure and Algorithm Design
5. Code is in question5code.py  
The algorithm needs to get the second smallest element. The second smallest node will always either be a sibling to the smallest node, or a parent of the smallest node. My code will loop through the left most branch of a binary search tree until the current nodes left grandchild is None. This ensures that when the loop breaks, the current node is always the parent of the smallest node. If the node contains a node to its right, then it would be the sibling of the smallest node, making it the second smallest node. If there is no node on its right, then the parent is the second smallest node.  
<br>
Assuming the binary search tree is balanced, the time complexity of my algorithm should be O(log(n)), since the time it takes to get to the leftmost node is related to the height of the tree, rather than the size of the input.  
<br>

6. Code is in question6code.py  
The algorithm reverses a singly linked list. In order to do this, three variables are needed. One to store the current node, one to store the next node, and one to store the previous node. First you store the next node in a separate variable, then say the next node is the previous node. Then set the previous node equal to the current node. Finally set the current node equal to the next node.  
<br>
Basically:  
a->b->c->None  
None<-a b->c  
None<-a<-b c  
None<-a<-b<-c  
c->b->a->None  
<br>

7. Code is in question7code.py  
<br>
The question states to find all anagrams of a given word within a given dictionary of 500,000 words. There are two main ways I could implement this.  
<br>
The first way is to find all possible letter combinations of the given word and then check if any combinations are in the dictionary.  
<br>
The second way is to iterate through the dictionary and check each entry to see if it is an anagram of the given word.  
<br>
Using math you can conclude the first way would be more practical. The second way will always search all 500,000 entries in the given dictionary. The second way will usually not perform that many operations. The way to calculate all possible combinations of a word is by using factorials. The closest factorial to 500,000 is 9!(1x2x3x4x5x6x7x8x9) which equals 362,880. So as long as the given word is 9 letters or less, it should be more efficient to calculate all possible letter combinations, then check if each combination is in the dictionary.
<br>
I looked at an implementation using pseudo-code for both methods, and they both have a time-complexity of O(n^2). The first method of iterating over the entire dictionary was much easier to implement however.