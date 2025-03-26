# Analysis
I reused and modified the bfs code I used for a previous assignment in this class.  

I think the algorithm I made is optimal. I chose bfs over dfs, because it makes more sense to me to check adjacent nodes on your level before decending to the next level of nodes. I don't think it would matter in either case though.  
The code is very simple. There is a list of possible colors in a set order. Each node is assigned the first possible color after removing the colors of everything touching it.  

# Limitations
The only limitation is that I used a set list of colors. This means if more colors are needed than what is in the list, the program will crash. This can be fixed by adding more colors to the list.  
At first I was planning on using numbers (color1, color2, color3, etc). But I thought if someone actually was going to use this algorithm, they would probably modify it to use actual colors, so I used actual colors.