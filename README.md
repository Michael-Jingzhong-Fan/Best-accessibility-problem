# Best-accessibility-problem

I start with a 2d array filled with 0s of all the blocks in the city. For every pizzeria in the city,
I create another 2d array of the same dimensions as the entire city and fill all blocks the pizzeria 
can deliver to with 1s and the rest with 0s. I sum the arrays and return the maximum value in the array.
throughout the code, I perform sanity checks on the input. Numpy is used both for ease of use and for
greater speed. I could flip the 2d arrays that contain the reachable blocks of the pizzeria to match 
the indexing of the 2d array to the question, however as the question only asks for the maximum pizza 
variety and not the position where one can obtain the maximum, flipping is not necessary.
