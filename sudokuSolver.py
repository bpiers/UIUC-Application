#solves sudoku puzzles
#written by bpiers
#improve by detecting unsolvable sudoku puzzles
size = 3
gridSize = size * size

#creates a sudoku grid of 0s
def makeGrid(gridSize) :
    gridRow=[]
    grid0=[]
    for i in range(0, gridSize**2) :
        gridRow.append(0)
        if len(gridRow) == gridSize :
            grid0.append(gridRow)
            gridRow = []
    return grid0

#creates copy of sudoku grid
def copyGrid(originalGrid) :
    newGrid = makeGrid(gridSize)
    for i in range(0, gridSize) :
        for j in range(0, gridSize) :
            newGrid[i][j] = originalGrid[i][j]
    return newGrid

#checks if newNumber is unique in set of compareNumbers
def uniqueCheck(newNumber, compareNumbers) :
    for currentNumber in compareNumbers :
        if newNumber == currentNumber :
            return False
    return True

#groups numbers from a Row into an array
def Row(i, currentGrid) :
    row = currentGrid[i][:]
    #print(row)
    return row

#groups numbers from a Column into an array
def Column(j, currentGrid) :
    column = []
    for n in range(0, gridSize) :
        column.append(currentGrid[n][j])
    #print(column)
    return column

#groups numbers from a Box into an array
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

#checks newNumber against Row, Column, and Box for uniqueness
#ensures newNumber abides by sudoku rules
def checkRowColumnBox(newNumber, currentGrid, i, j) :
    result = []
    checkThese = [Row(i, currentGrid), Column(j, currentGrid), Box(i,j, currentGrid)]
    for this in checkThese :
        result = uniqueCheck(newNumber, this)
        if result == False :
            return False
    return True

#prints sudoku grid as a matrix
#old function to print sudoku grid
def printGridMatrix(inputGrid) :
    row = []
    for i in range(0, len(inputGrid[0])) :
        for j in range(0, len(inputGrid[0])) :
            row.append(inputGrid[i][j])
            if len(row) == len(inputGrid[0]) :
                print(row)
                row = []
    return

#prints sudoku grid as stylized grid
def printGrid(inputGrid) :
    rowLength = size ** 2
    i1 = 0
    i2 = 0
    for i in range(0, rowLength) :
        for j in range(0, rowLength) :
            if inputGrid[i][j] == 0 :
                print('_', end='  ')
            else :
                print(inputGrid[i][j], end='  ')
            if i1%rowLength != rowLength - 1 :
                if i1%size == size - 1 :
                    print('|', end='  ')
            else :
                print('')
                if i1%(rowLength*3) == rowLength*3 - 1 and i1 < rowLength**2 - 1:
                    print('---------+-----------+---------')
            i1 = i1 + 1
    return

#moves the focues of solver function to previous cell
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
                    print('Failed to solve.')
                    return gridSize, gridSize
                return i, j
            if j == 0 :
                i = i - 1
                j = gridSize
    print('Failed to solve.')
    return gridSize, gridSize

#moves the focus of solver function to next cell
def moveForward(problem, i, j) : #still need to fix this
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

#solves the sudoku puzzle
def solver(problem) :
    if not validateSolution(problem) :
        return False
    print('attempting to solve sudoku puzzle...')
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
            for guess in range(progress[i][j] + 1, gridSize+1) :
                guessResult = checkRowColumnBox(guess, progress, i, j)
                if guessResult == True :
                    progress[i][j] = guess
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
                if guess == gridSize :
                    progress[i][j] = 0
                    move = moveBack(problem, i, j)
                    i = move[0]
                    j = move[1]
                    #print('back     i'+str(i)+' j'+str(j)+' '+str(progress[i][j]))
                    while progress[i][j] == gridSize :
                        progress[i][j] = 0
                        move = moveBack(problem, i, j)
                        i = move[0]
                        j = move[1]
    validateSolution(progress)
    return progress

def validateSolution(solution) :
    for i in range(0, gridSize) :
        for j in range(0, gridSize) :
            temp = solution[i][j]
            if temp == 0 :
                continue
            solution[i][j] = -1
            flag = checkRowColumnBox(temp, solution, i, j)
            solution[i][j] = temp
            if not flag :
                print('failed validation check. puzzle does not meet sudoku rules.')
                return flag
    return flag

#user enters numbers from their sudoku puzzle
#user choice (1) calls this function
def enterProblem() :
    problemGrid = makeGrid(gridSize)
    for i in range(0, gridSize) :
        for j in range(0, gridSize) :
            inputNumber = -1
            while inputNumber < 0 or inputNumber > gridSize :
                if inputNumber != -1 :
                    print('Number not 1-9. ', end='')
                print('Enter number : ', end='')
                inputNumber = input()
                if inputNumber == '' :
                    inputNumber = 0
                try :
                    inputNumber = int(inputNumber)
                except ValueError :
                    print('Not a valid number. ', end='')
                    inputNumber = -1
            problemGrid[i][j] = inputNumber
            printGrid(problemGrid)
    return problemGrid

#test cases to validate changes to program
#user choice (2) calls this function
def runTest() :
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

    fails =   [[7,9,0,0,0,0,0,5,0],
               [4,0,0,6,0,0,0,0,0],
               [0,9,0,7,4,2,0,6,0],
               [0,7,9,5,0,0,0,4,8],
               [0,0,0,0,0,0,0,0,0],
               [8,3,0,0,0,4,9,1,0],
               [0,4,0,1,2,9,0,0,0],
               [0,0,0,0,0,6,0,0,7],
               [0,6,0,0,0,0,0,9,3]]
    testCases = [grid, gridOG, gridOG2, gridOG3, gridOG4, gridOG5, gridOG6, hardest, fails]
    #run some tests to see if you broke anything
    print('solving test sudoku grids...')
    i = 0
    for test in testCases :
        i = i + 1
        print('Sudoku Puzzle ' + str(i) + ' of ' + str(len(testCases)))
        printGrid(test)
        attempt = solver(test)
        if attempt :
            printGrid(attempt)
        print('')
    print('success!')

#main function
print('Select feature.')
print('    (1) Enter suduko problem to be solved.')
print('    (2) Run example cases.')
print('    (3) Exit program.')
print('Enter feature number : ', end='')
selection = input()
if selection == '1' :
    attempt = solver(enterProblem())
    if attempt :
        printGrid(attempt)
elif selection == '2' :
    runTest()
else :
    print('exiting program')
