
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Given an n by n grid of letters, and a list of words, find the location in the grid where the word can be found. A word matches a straight, contiguous line of letters in the grid. The match could either be done horizontally (left or right) or vertically (up or down) or along any diagonal either right to left or from left to right.

Input: 

The input will be in a file word_grid.in. Do not hard code the name of the file in your program. You will read the file from stdin. Here is the format of the input file. Assume that the format is correct; that is you do not have to do any error checking.

- First line will have one integer - n, the number of lines in the grid and the number of characters in each line.

- There will be a single blank line.

- There will be n lines, where each line will have n characters, all in upper case, separated by a space.

- There will be a single blank line.

- There will be a single integer k, denoting the number of words that follow.

- There will be k lines. Each line will contain a single word in all uppercase.

Output: 

There will be k lines in your output. Each line will have the word that you are to search, followed by a colon, followed by a single space and then the tuple giving the row and column where you found the word. In the tuple you will have two integers (i, j). The number i gives the row and the number j the column of the first letter of the word that you were required to find. Rows and columns are numbered conventionally, i.e. the first row is 1 and the first column is 1. If you do not find a word in the grid then the values for i and j will be 0 and 0. Use the full power of the built-in functions associated with strings and lists. This is the output (https://www.cs.utexas.edu/users/mitra/csSpring2022/cs313/assgn/found.out) for the given input file.
