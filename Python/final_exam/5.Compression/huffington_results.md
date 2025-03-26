# Analysis
For this problem I mostly reused my code from the previos assignment where we used the Huffington Compression algorithm.  

After compressing JINGLEBELLS, the compressed size was 57 bits compared to the 44 bits that would have been used if I did fixed encoding instead. This means the compressed string was actually about 30% bigger than if I didn't try to compress it.  

I believe this is because we were provided with an already constructed frequency table. The table contained many symbols with high frequency that were not present in the input string. This lead to many of the codes for JINGLEBELLS being over 4 bits in length.  

It seems like this compression method seems to work best when used with the strings that made the table in the first place. It might be better to create multiple huffington trees for different compressions.