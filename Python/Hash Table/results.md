# Separate Chaining
## Test
For the test I tried inserting 100 elements into a hash table of size 12. Upon collision I just added
the new element as the head of a list connected to other nodes with the same index.
All 100 elements were able to fit in the table.
## Analysis
Unlike the other two hash tables, I was able to fit all elements into this hash table. Overall, there were less collisions,
since the collision is dealt with the first time it happens, without trying a new index. Insertion time is constant, whereas
search and delete are dependent on how many elements are in each bucket. The downside of this method is that it can take up much more
space than the other two methods, since it stores all elements inserted. 
# Linear Probe
## Test
I tried inserting 100 elements into a table of size 101. I chose a size only 1 higher than the amount of elements, to promote collision, while still making it possible to insert all elements. The table was only able to insert about 97 items on average. I set it so
it would stop trying to insert a value after table_size/4 tries, so in the case of 101, about 25 tries. This results in a lot of collsions,
but prevents infinite loops.
## Analysis
While linear probing stores less than separate chaining, that may be considered a good thing in some cases. The major downside
seems to be with the skip mechanism on insertion. Skipping by a static value tends to lead to clustering, which overall makes
colliosion more likely to happen.
# Double Hash
## Test
Very similar to linear probing. I tried inserting 100 elements into a table of size 101. The double hashing table was able to insert all elements about half the time. It did better than the linear probing method.
## Analysis
While the coding for the double hashing table was extremely similar to linear probing, skipping by a variable amount seemed to make a significant impact. When testing the linear probing method it almost never was able to insert all 100 elements, but with double hashing, it happened about 50% of the time.