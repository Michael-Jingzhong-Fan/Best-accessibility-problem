import numpy as np

#Get-Content input2.txt | python3 pizzeria_solution.py

def load_file(fileName):
    #Remove \n
    lines = open(fileName).read().split('\n')
    #Remove whitespace
    firstLine = lines[0].split()
    
    #Grid dimensions
    dimension = int(firstLine[0])
    #Number of pizzerias
    inputNumber = int(firstLine[1])
    
    #Pizzeria info
    info = []
    for i in range(1,inputNumber + 1):
        line = [int(l) for l in lines[i].split()]
        info.append(line)
      
    return dimension, inputNumber, info  
    
class Block():
    def __init__(self, dimension, currentBlock, maximumDistance):
        #Sanity checks
        
        if (maximumDistance < 1) or (maximumDistance > 100):
            raise Exception('Pizzeria range cannot be 0 or exceed 100')

        if (currentBlock[0] < 1) or (currentBlock[1] > dimension):
            raise Exception('Pizzeria currentBlock not within {} x {}'.format(dimension,dimension))

        if (dimension < 1) or (dimension > 1000):
            raise Exception('dimensions not between 1 and 1000')

        
        self.dimension = dimension
        self.currentBlock = currentBlock 
        self.maximumDistance = maximumDistance 
        self.block = np.zeros((dimension,dimension))
        
    def build_block(self):
        '''
        Build a 2D array showing the range of the pizzeria. 
        Within range set to 1, outside range set to 0. 
        '''
        x = self.currentBlock[0] - 1
        y = self.currentBlock[1] - 1
        
        for i in range(self.maximumDistance + 1):
            # get vertical and horizontal
            if (y+i) < dimension:
                self.block[x][y+i] = 1
            if (y-i) >= 0:
                self.block[x][y-i] = 1
            if (x+i) < dimension:
                self.block[x+i][y] = 1
            if (x-i) >= 0:
                self.block[x-i][y] = 1

        for i in range(1,self.maximumDistance):
            # get diagonals 
            if (x+i < dimension) & (y-i >= 0):
                self.block[x+i][y-i] = 1
            if (x-i >= 0) & (y+i < dimension):
                self.block[x-i][y+i] = 1
            if (x+i < dimension) & (y+i < dimension):
                self.block[x+i][y+i] = 1
            if (x-i >= 0) & (y-i >= 0): 
                self.block[x-i][y-i] = 1
        
        #Flip block upside down to match indexing in question. 
        #Default indexing (0,0) on top left corner
        #Question requires indexing (0,0) at bottom left corner
        
        self.block = np.flipud(self.block)
          
            
        return self.block
    

if __name__ == '__main__':
    fileName = 'input2.txt'
    
    # extract data
    dimension, pizzeriaNumber, pizzerias = load_file(fileName)
    
    sumRange = np.zeros((dimension,dimension))

    for pizzeria in pizzerias:
        block = Block(dimension, pizzeria[0:-1], pizzeria[-1])
        pizzaRange = block.build_block()
        sumRange += pizzaRange
    
    # print(sumRange)
    print(int(np.max(sumRange)))
    
    
    
    