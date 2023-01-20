#  File: WordSearch.py

#  Description: The following program finds the first placement of words in a grid and returns the location where the first letter is found.

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 1/25/22

#  Date Last Modified: 1/28/22

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    # instantiate 2-D list that contains each letter in word search
    letter = []
    # list that contains words to search
    words =  []
    # stores number of lines
    num_lines = sys.stdin.readline()
    # skip over whitespace
    whitespace = sys.stdin.readline()
    
    # loops through num_lines lines
    for i in range(int(num_lines)):
        # creates a list of letters in ith line
        temp = sys.stdin.readline().split()
        # appends each element of temp into 2-D list (i denotes row and j denotes col)
        letter.append(temp)
    
    # skip over whitespace
    whitespace = sys.stdin.readline()
    # stores number of words
    num_words = sys.stdin.readline()
    
    # loops through num_words lines
    for i in range(int(num_words)):
        # appends each line into words
        words.append(sys.stdin.readline().strip())
        
    # returns 2-D list of letters and 1-D list of words to search for
    return (letter, words)

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid

def find_word (grid, word):
    # begins with the first row
    row = 0
    
    while (row < len(grid)):
        # traverses through the columns of each row, beginning with the first column of the first row
        # loop continues until all possible columns are traversed or conditional statements are met
        for column in range(len(grid[row])):
            
            if column + len(word) <= len(grid[row]): # establishes bound for search to the right
                columnnumber = column # new variable that is modified to search through columns
                lst = []
                for i in range(len(word)):
                    lst.append(grid[row][columnnumber])
                    columnnumber += 1
                if lst == list(word.strip()): # assess whether list containing letters from search matches the word to be found
                    return (row + 1, column + 1)
                
            if column - len(word) >= -1: # establishes bound for search to the left
                columnnumber = column # new variable that is modified to search through columns
                lst = []
                for i in range(len(word)):
                    lst.append(grid[row][columnnumber])
                    columnnumber -= 1
                if lst == list(word.strip()): # assess whether list containing letters from search matches the word to be found
                    return (row + 1, column + 1)
                
            if row + len(word) <= len(grid): # establishes bound for downwards search
                rownumber = row # new variable that is modified to search through rows
                lst = []
                for i in range(len(word)):
                    lst.append(grid[rownumber][column])
                    rownumber += 1
                if lst == list(word.strip()): # assess whether list containing letters from search matches the word to be found
                    return (row + 1, column + 1)
                
            if row - len(word) >= -1: # establishes bound for upwards search
                rownumber = row # new variable that is modified to search through rows
                lst = []
                for i in range(len(word)):
                    lst.append(grid[rownumber][column])
                    rownumber -= 1
                if lst == list(word.strip()): # assess whether list containing letters from search matches the word to be found
                    return (row + 1, column + 1)

            if (row + len(word) <= len(grid)) and (column + len(word) <= len(grid[row])): # establishes bound for diagonal search to the bottom right
                columnnumber = column # new variable that is modified to search through columns
                rownumber = row # new variable that is modified to search through rows
                lst = []
                for i in range(len(word)):
                    lst.append(grid[rownumber][columnnumber])
                    rownumber += 1
                    columnnumber += 1
                if lst == list(word.strip()): # assess whether list containing letters from search matches the word to be found
                    return (row + 1, column + 1)
                
            if (row + len(word) <= len(grid)) and (column - len(word) >= -1): # establishes bound for diagonal search to the bottom left
                columnnumber = column # new variable that is modified to search through columns
                rownumber = row # new variable that is modified to search through rows
                lst = []
                for i in range(len(word)):
                    lst.append(grid[rownumber][columnnumber])
                    rownumber += 1
                    columnnumber -= 1
                if lst == list(word.strip()): # assess whether list containing letters from search matches the word to be found
                    return (row + 1, column + 1)
                
            if (row - len(word) >= -1) and (column + len(word) <= len(grid[row])): # establishes bound for diagonal search to the top right
                columnnumber = column # new variable that is modified to search through columns
                rownumber = row # new variable that is modified to search through rows
                lst = []
                for i in range(len(word)):
                    lst.append(grid[rownumber][columnnumber])
                    rownumber -= 1
                    columnnumber += 1
                if lst == list(word.strip()): # assess whether list containing letters from search matches the word to be found
                    return (row + 1, column + 1)
                
            if (row - len(word) >= -1) and (column - len(word) >= -1): # establishes bound for diagonal search to the top left
                columnnumber = column # new variable that is modified to search through columns
                rownumber = row # new variable that is modified to search through rows
                lst = []
                for i in range(len(word)):
                    lst.append(grid[rownumber][columnnumber])
                    rownumber -= 1
                    columnnumber -= 1
                if lst == list(word.strip()): # assess whether list containing letters from search matches the word to be found
                    return (row + 1, column + 1)
                
        # proceed to the next row if search in the current row fails
        row += 1
        
    # return the following tuple if word is not located in the grid
    return (0, 0)

def main():
  # read the input file from stdin
  word_grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
    location = find_word (word_grid, word)
    print (word + ": " + str(location))

if __name__ == "__main__":
    main()
