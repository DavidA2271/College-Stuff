# Analysis
## Compression Ratio
I ran my compression algorithm on a variety of strings. I did a single character, two characters, multiple of a single character, multiple different characters, and multiple characters with special characters.  
The algorithm seemed to have the highest compression ratio on strings with less variance in input characters. A string with one input character "a" had and 85% reduction in size, while the string "aaaaaaaaaaaaaaaaaa" also had an 85% reduction. It makes sense, since "a" was reduced by 85%, having several "a"s would keep the same reduction proportion.  
The lowest compression reduction I got was 0%. I input every single character on my keyboard exactly once. The original string had a size of 641 bits, compressed 635 bits. So only 6 bits less.  
The Huffman Compression algorithm seems like it works best when there is less variance in the input string, but overall, it seemed to always reduce the size of an input string.
## Error Detection
Checksum seems like a very useful tool to check if data has been corrupted. Checking the sum or the original ascii and comparing it to the decoded string seems like it would work most of the time. Maybe it would be possible for the checksum to remain the same even if the data corrupted in some weird way. I don't know.  
