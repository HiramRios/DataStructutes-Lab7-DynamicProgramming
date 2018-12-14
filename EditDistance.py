''' Hiram Rios 80552404 computer science 
the purpose of this lab is to get familiar with dynamic programing by coding the 
edit distance method 

'''
def edit_distance(first, second):
    # this creates an integer based on the length of the words 
    #thats are provided
    firstWord = len(first)+1
    secondWord = len(second)+1
    # this table will create the matrix in which you will do the 
    # operations for the distance 
    table = {}
    
    for i in range(firstWord): table[i,0]=i #creates sized array for word 1
    for j in range(secondWord): table[0,j]=j #creates sized array for word 2
    
    for i in range(1, firstWord):
        for j in range(1, secondWord):
            # the costs of will be 0 if the letters equal the same 
            cost = 0 if first[i-1] == second[j-1] else 1
            table[i,j] = min(table[i, j-1]+1, table[i-1, j]+1, table[i-1, j-1]+cost)

    return table[i,j] #returns the edit distance value
 
word1 = input("Enter your first word:")
word2 = input("Enter your second word:")

print("Edit distance: ", edit_distance(word1, word2))