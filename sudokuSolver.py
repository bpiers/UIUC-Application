#Easy Puzzle 4,682,668,579 from https://www.websudoku.com/?level=1&set_id=4682668579
# second puzzle https://www.websudoku.com/?level=1&set_id=3948377814
size = 3
gridSize = size * size
grid =    [[7,1,0,9,0,0,0,0,8],
           [0,0,0,0,0,6,9,0,0],
           [9,6,0,4,1,0,0,0,0],
           [0,0,0,0,9,2,8,6,3],
           [3,0,9,0,6,0,2,0,1],
           [2,8,6,3,5,0,0,0,0],
           [0,0,0,0,8,3,0,4,9],
           [0,0,3,5,0,0,0,0,0],
           [1,0,0,0,0,9,0,3,2]]

gridOG =  [[7,1,0,9,0,0,0,0,8],
           [0,0,0,0,0,6,9,0,0],
           [9,6,0,4,1,0,0,0,0],
           [0,0,0,0,9,2,8,6,3],
           [3,0,9,0,6,0,2,0,1],
           [2,8,6,3,5,0,0,0,0],
           [0,0,0,0,8,3,0,4,9],
           [0,0,3,5,0,0,0,0,0],
           [1,0,0,0,0,9,0,3,2]]

solution =[[7,1,4,9,3,5,6,2,8],
           [8,3,5,2,7,6,9,1,4],
           [9,6,2,4,1,8,3,7,5],
           [5,4,1,7,9,2,8,6,3],
           [3,7,9,8,6,4,2,5,1],
           [2,8,6,3,5,1,4,9,7],
           [6,2,7,1,8,3,5,4,9],
           [4,9,3,5,2,7,1,8,6],
           [1,5,8,6,4,9,7,3,2]]

gridOG2 = [[0,0,0,7,0,0,0,0,8],
           [4,0,0,0,0,0,0,3,0],
           [0,8,0,5,3,0,4,0,7],
           [0,6,0,0,0,7,0,0,0],
           [8,0,2,0,0,0,5,0,6],
           [0,0,0,9,0,0,0,1,0],
           [1,0,8,0,6,4,0,7,0],
           [0,4,0,0,0,0,0,0,3],
           [7,0,0,0,0,5,0,0,0]]

gridOG3 = [[0,2,0,0,3,0,2,0,0],
           [0,8,0,4,0,0,0,0,0],
           [0,2,0,0,0,5,0,6,1],
           [0,9,0,1,0,0,0,7,0],
           [2,0,0,0,4,0,0,0,9],
           [0,3,0,0,0,9,0,8,0],
           [3,1,0,7,0,0,0,4,0],
           [0,0,0,0,0,4,0,5,0],
           [0,0,6,0,9,0,0,2,0]]

gridOG4 = [[0,1,6,2,3,0,0,0,9],
           [0,8,0,0,0,0,0,0,0],
           [0,0,0,1,0,7,0,0,5],
           [0,0,0,0,0,4,0,9,8],
           [0,0,1,0,0,0,3,0,0],
           [8,2,0,6,0,0,0,0,0],
           [6,0,0,4,0,1,0,0,0],
           [0,0,0,0,0,0,0,7,0],
           [3,0,0,0,6,8,4,2,0]]

hardest = [[8,0,0,0,0,0,0,0,0],
           [0,0,3,6,0,0,0,0,0],
           [0,7,0,0,9,0,2,0,0],
           [0,5,0,0,0,7,0,0,0],
           [0,0,0,0,4,5,7,0,0],
           [0,0,0,1,0,0,0,3,0],
           [0,0,1,0,0,0,0,6,8],
           [0,0,8,5,0,0,0,1,0],
           [0,9,0,0,0,0,4,0,0]]

gridOG5 = [[0,2,8,1,0,0,0,0,0],
           [4,0,0,0,8,0,0,3,0],
           [0,0,0,0,2,0,0,0,0],
           [7,3,0,0,0,0,0,0,6],
           [0,0,4,0,0,0,8,5,0],
           [0,0,5,0,0,9,0,0,0],
           [0,0,2,0,3,6,0,0,9],
           [8,0,0,9,0,0,0,0,7],
           [0,6,0,2,0,0,0,4,0]]

gridOG6 = [[7,9,0,0,0,0,0,5,0],
           [4,0,0,6,0,0,0,0,0],
           [0,0,0,7,4,2,0,6,0],
           [0,7,9,5,0,0,0,4,8],
           [0,0,0,0,0,0,0,0,0],
           [8,3,0,0,0,4,9,1,0],
           [0,4,0,1,2,9,0,0,0],
           [0,0,0,0,0,6,0,0,7],
           [0,6,0,0,0,0,0,9,3]]

def makeGrid(gridSize) : #creates a blank sudoku grid
    gridRow=[]
    grid0=[]
    for i in range(0, gridSize**2) :
        gridRow.append(0)
        if len(gridRow) == gridSize :
            grid0.append(gridRow)
            gridRow = []
    return grid0

def copyGrid(originalGrid) :
    newGrid = makeGrid(gridSize)
    for i in range(0, gridSize) :
        for j in range(0, gridSize) :
            newGrid[i][j] = originalGrid[i][j]
    return newGrid


def uniqueCheck(newNumber, compareNumbers) :
    #number is what the user inputed.
    #cell is the [row,column] of the number
    for currentNumber in compareNumbers :
        if newNumber == currentNumber :
            return False
    return True


def Row(i, currentGrid) :
    row = currentGrid[i][:]
    #print(row)
    return row

def Column(j, currentGrid) :
    column = []
    for n in range(0, gridSize) :
        column.append(currentGrid[n][j])
    #print(column)
    return column

def Box(i,j, currentGrid) :
    boxRowLoc = int(i/(gridSize**(0.5)))*size
    #print(boxRowLoc)
    boxColumnLoc = int(j/(gridSize**(0.5)))*size
    #print(boxColumnLoc)
    box = []
    for x in range(0, size) :
        for y in range(0, size) :
            box.append(currentGrid[boxRowLoc+x][boxColumnLoc+y])
    #print(box)
    return box

def checkRowColumnBox(newNumber, currentGrid, i, j) :
    result = []
    checkThese = [Row(i, currentGrid), Column(j, currentGrid), Box(i,j, currentGrid)]
    for this in checkThese :
        result = uniqueCheck(newNumber, this)
        if result == False :
            return False
    return True

#grid = makeGrid(gridSize)
def printGrid(inputGrid) :
    row = []
    for i in range(0, len(inputGrid[0])) :
        for j in range(0, len(inputGrid[0])) :
            row.append(inputGrid[i][j])
            if len(row) == len(inputGrid[0]) :
                print(row)
                row = []
    return



def solver2(guesses) :
    for i in range(0, gridSize) :
        for j in range(0, gridSize) :
            #print('i'+str(i)+' j'+str(j))
            if guesses[i][j] != 0 :
                return
    return

def moveBack(problem, x, y) :
    i = x
    j = y
    if j == 0 and problem[i][j] == 0 :
        i = i - 1
        j = gridSize
    while i >= 0 :
        while j >= 0 :
            if j > 0 :
                j = j - 1
            if problem[i][j] == 0 :
                if i<0 or j<0 :
                    print('failed to solve')
                    return False
                return i, j
            if j == 0 :
                i = i - 1
                j = gridSize
    print('i have failed to solve your sudoku. *performs seppuku*')
    return False

def moveForward(problem, x, y) : #still need to fix this
    i = x
    j = y
    j = j + 1
    if j >= gridSize :
        i = i + 1
        j = 0
        if i >= gridSize :
            print('sudoku solved')
            return i,j
    while problem[i][j] != 0 :
        j = j + 1
        if j >= gridSize :
            i = i + 1
            j = 0
            if i >= gridSize :
                print('sudoku solved')
                return i,j
    return i, j
    # while i < gridSize and j < gridSize :
    #     if j >= gridSize :
    #         i = i + 1
    #         j = 0
    #     while j <= gridSize :
    #         if problem[i][j] == 0 :
    #             return i, j
    #         if j == gridSize :
    #             i = i + 1
    #             j = 0
    # print('i have solved your sudoku.')
    # return False

def solver3(problem) :
    killSwitch = 0
    progress = copyGrid(problem)
    i = 0
    j = 0
    if progress[0][0] != 0 :
        f = moveForward(problem, i, j)
        i = f[0]
        j = f[1]
        #print(i,j)
    while i < gridSize :
        while j < gridSize :
            killSwitch = killSwitch + 1
            if killSwitch > 1000000 :
                print('timed out. killSwitch activated')
                return progress
            for attempt in range(progress[i][j] + 1, gridSize+1) :
                attemptResult = checkRowColumnBox(attempt, progress, i, j)
                if attemptResult == True :
                    progress[i][j] = attempt
                    #print('write '+str(progress[i][j])+'  i'+str(i)+' j'+str(j))
                    move = moveForward(problem, i, j)
                    i = move[0]
                    j = move[1]
                    if i >= gridSize :
                        j = gridSize
                        break
                    progress[i][j] = 0
                    #print('forward  i'+str(i)+' j'+str(j))
                    break
                if attempt == gridSize :
                    progress[i][j] = 0
                    move = moveBack(problem, i, j)
                    i = move[0]
                    j = move[1]
                    #print('back     i'+str(i)+' j'+str(j)+' '+str(progress[i][j]))
                    if progress[i][j] == gridSize : #this is an example of bad code
                        progress[i][j] = 0
                        move = moveBack(problem, i, j)
                        i = move[0]
                        j = move[1]
                        #print('back2    i'+str(i)+' j'+str(j)+' '+str(progress[i][j]))
                        if progress[i][j] == gridSize : #this is even worse
                            progress[i][j] = 0
                            move = moveBack(problem, i, j)
                            i = move[0]
                            j = move[1]
                            #print('back3    i'+str(i)+' j'+str(j)+' '+str(progress[i][j]))
                            if progress[i][j] == gridSize : #not even trying at this point
                                progress[i][j] = 0
                                move = moveBack(problem, i, j)
                                i = move[0]
                                j = move[1]
                                print('back4    i'+str(i)+' j'+str(j)+' '+str(progress[i][j]))
    #print(killSwitch)
    return progress

printGrid(gridOG6)
print('')
printGrid(solver3(gridOG6))
