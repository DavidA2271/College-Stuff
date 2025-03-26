# Comparison
There was a big difference in the implementation for KMP and REGEX. KMP was a little confusing to understand why it worked, but after running through a few examples it made more sense. It took a bit to implement, but now it should work to find any substring in a string.  
The implementation of REGEX was a lot simpler. I was confused by it for the first example, but after that it made a lot more sense. There is a lot less coding involved with REGEX.  

The challenge with KMP was understanding why it worked. The challenge with REGEX was figuring out what all of the symbols meant and how to combine them to get my desired result.  

KMP seems more suitable for finding many different substrings. For any new kind of substring, a new REGEX pattern is needed, which is unsuitable for a regular person with little coding knowledge to use. It also requires more overhead from coders if there are several patterns that are needed.  
However, if you are doing somethig simple, like finding all dates or something with a predictable pattern, REGEX does very well and should be used in those scenarios.  

It is important to know both methods, so that when you face a situation where one or the other is needed, you know which one to choose.

# REGEX Explanation
## Email
[.A-Za-z0-9]+@[.A-Za-z0-9]+  
Emails follow a simple pattern of username@url. I used this to make the above REGEX pattern.  
[.A-Za-z0-9]+ matches with any letter number or dot that may be in the username. The plus sign mathes these until it finds something that does not match with the pattern. I follow it with @ to denote a url is next. That is then followed by the first pattern to detect any dots, letters, or numbers. The pattern ends upon hitting a space or end of line since they are not dots, letters, or numbers.
## Date
[0-9]+\/[0-9]+\/[0-9]+  
[0-9]+-[0-9]+-[0-9]+  
[A-Za-z]+ [0-9]+, [0-9]+  
I had three patterns for the three different date formats. When I made the patters, I didn't know I could possibly condense them into a single pattern or two instead of three. I decided to keep three patterns after I figured out how though.  
The first patterns are very similar. They search for numbers until they hit either a \ or -. Then continue that pattern tow more times, not looking for \ or - the last time.  
The third pattern searches for letters, space, numbers, space, then numbers again.
## Phone
(\(|\+|)([0-9]+)(\)|)(.)([0-9].+)  
I figured out how exactly to use grouping and conditions on this example. The file you provided had four different phone number formats, and this one REGEX pattern can capture all of them.  
(\(|\+|) looks confusing but can be broken down into simpler parts.  
(  \(  |  \+  |  ) The surrounding parenthesis indicate a grouping. the \( 'escapes' the ( character. This means i can search for that character even though it is a REGEX special character. The | is an OR operator. (\(|\+|) has two ORs. It searches for \ or + or nothing. Some phone numbers do not start with ( or +.  
After that first part, I search for numbers, then optionally ), then I used the dot character. In REGEX '.' represents any character. All presented phone number formats had something separating number groups and this dot can always account for that something.
## URL
(http|https|ftp)([^ ]+)  
This pattern searches for a substring that starts with either https, https, or ftp and continues until it hits a space.
## Color Codes
(#)([A-Za-z0-9]+)  
This pattern searches for the pound character and gets all letters and numbers until a space.