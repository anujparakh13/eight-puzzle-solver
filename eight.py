import numpy as np
from time import sleep

#
# GLOBAL VARIABLES
#
depth = 0
nodesVisited = []
goalState = [1, 2, 3, 8, 0, 4, 7, 6, 5]
winnerFound = False
numNodesVisited = 0


# Each Node stores the game array and the steps used to get there
class Node:
    def __init__(self, gameArray, steps):
        self.gameArray = gameArray
        self.steps = steps
    
    def __repr__(self):
        return '( ' + str(self.gameArray) + ', ' + self.steps + ')'


    def __str__(self):
        return '( ' + str(self.gameArray) + ', ' + self.steps + ')'

# Each Node stores the game array and the steps used to get there
class NodeInformed:
    def __init__(self, gameArray, steps, fValue):
        self.gameArray = gameArray
        self.steps = steps
        self.fValue = fValue
    
    def __repr__(self):
        return 'NI: ( ' + str(self.gameArray) + ', ' + self.steps + ', ' + str(self.fValue) + ')'


    def __str__(self):
        return '( ' + str(self.gameArray) + ', ' + self.steps + ', ' + str(self.fValue) + ')'


#
# COMMON FUNCTIONS : Used by all solution methods
#

# Returns an array of possible motions as an array
def getPossibleMotions(gameArray):
    possibleMotions = []
    # Add possible movements        
    possibleMotions.append('UP') if (gameArray.index(0) > 2) else 0
    possibleMotions.append('DOWN') if (gameArray.index(0) < 6) else 0
    possibleMotions.append('LEFT') if (gameArray.index(0) % 3 > 0) else 0
    possibleMotions.append('RIGHT') if (gameArray.index(0) % 3 < 2)  else 0
    return possibleMotions

# Move the empty spot up (Assumes movement is possible)
def moveUp(gameArray):
    zeroPos = gameArray.index(0)
    # Swap required positions
    gameArray[zeroPos], gameArray[zeroPos - 3] = gameArray[zeroPos - 3], gameArray[zeroPos]

    return gameArray

# Move the empty spot down (Assumes movement is possible)
def moveDown(gameArray):
    zeroPos = gameArray.index(0)
    # Swap required positions
    gameArray[zeroPos], gameArray[zeroPos + 3] = gameArray[zeroPos + 3], gameArray[zeroPos]
    return gameArray

# Move the empty spot right (Assumes movement is possible)
def moveRight(gameArray):
    zeroPos = gameArray.index(0)
    # Swap required positions
    gameArray[zeroPos], gameArray[zeroPos + 1] = gameArray[zeroPos + 1], gameArray[zeroPos]
    return gameArray

# Move the empty spot left (Assumes movement is possible)
def moveLeft(gameArray):
    zeroPos = gameArray.index(0)
    # Swap required positions
    gameArray[zeroPos], gameArray[zeroPos - 1] = gameArray[zeroPos - 1], gameArray[zeroPos]
    return gameArray

# Make the game array perform given movement type
def makeMovement(gameArray, moveType):
    if (moveType == 'UP'):
        return moveUp(gameArray)
    elif (moveType == 'DOWN'):
        return moveDown(gameArray)
    elif (moveType == 'RIGHT'):
        return moveRight(gameArray)
    elif (moveType == 'LEFT'):
        return moveLeft(gameArray)




# # # # # # # # # # # #
#                     #
# SOLUTION ALGORITHMS #
#                     #
# # # # # # # # # # # #


# # # # # # # # # #
#       DFS       #
# # # # # # # # # #

# Called when winner has been found using BFS
def winnerFoundDFS(node):
    print("WINNER FOUND")
    node.steps = node.steps [:-2] # remove the last ', '
    print ('Solution: ' + node.steps)
    print ('Number of nodes visited: ' + str(len(nodesVisited) + 1))
    print ('Max Node List Size: ')
    return


def expandNodeDFS(node):
     # in order to change value
    global depth
    # Update depth
    depth += 1
    nodesVisited.append(list(node.gameArray))
    movements = getPossibleMotions(node.gameArray)
    print ('Number of nodes visited: ' + str(len(nodesVisited)) + ', Current: ' + str(node.gameArray))

    for mov in movements:
        newGameArray = makeMovement(list(node.gameArray), mov)     
 
        # Check goal
        if (goalState == (newGameArray)):
            newNode = Node(newGameArray, node.steps + mov + ', ')
            winnerFoundDFS(newNode)
            break
        
        if not (newGameArray in nodesVisited):
            newNode = Node(newGameArray, node.steps + mov + ', ')
            expandNodeDFS(newNode)
    depth -= 1

def solveDFS(gameArray):
    print('Using DFS')
    expandNodeDFS(Node(gameArray, ''))


# # # # # # # # # #
#       BFS       #
# # # # # # # # # #

# Used to store nodes added to BFS Queue
bfsQueue = []

# Called when winner has been found using BFS
def winnerFoundBFS(node):
    print("WINNER FOUND")
    node.steps = node.steps [:-2] # remove the last ', '
    print ('Solution: ' + node.steps)
    print ('Number of nodes visited: ' + str(len(nodesVisited) + 1))
    print ('Max Node List Size: ')
    return

# Called to visit a node in BFS
def visitNodeBFS(node):
    global bfsQueue
    if (goalState == (node.gameArray)):
        winnerFoundBFS(node)
        bfsQueue = []
        return

    nodesVisited.append(node.gameArray)
    # print ('Number of nodes visited: ' + str(len(nodesVisited)))

    movements = getPossibleMotions(node.gameArray)
    for mov in movements:
        # Add each new movement as a child to the queue
        newGameArray = (makeMovement(list(node.gameArray), mov)) # Make movement and create next node
        if not (newGameArray in nodesVisited): # Make sure node is not visited already
            newNode = Node(newGameArray, node.steps + mov + ', ')
            bfsQueue.append(newNode)

def solveBFS(gameArray):
    root = Node(gameArray, '')
    visitNodeBFS(root)
    # As long as the queue isn't empty, keep visiting nodes
    while bfsQueue:
        visitNodeBFS (bfsQueue.pop(0))


# # # # # # # # # #
#       IDS       #
# # # # # # # # # #

# Called when winner has been found using BFS
def winnerFoundIDS(node):
    print("WINNER FOUND")
    node.steps = node.steps [:-2] # remove the last ', '
    print ('Solution: ' + node.steps)
    print ('Number of nodes visited: ' + str(numNodesVisited))
    print ('Max Node List Size: ')
    return

def visitNodeIDS(node, depthLimit):
    global depth, winnerFound, numNodesVisited
    numNodesVisited += 1

    if (winnerFound):
        return

    if (goalState == (node.gameArray)):
        winnerFoundIDS(node)
        winnerFound = True
        return

    if (depth == depthLimit):
        depth -= 1
        return
    
    # nodesVisited.append(node.gameArray)

    movements = getPossibleMotions(node.gameArray)
    for mov in movements:
        depth += 1
        newGameArray = (makeMovement(list(node.gameArray), mov)) # Make movement and create next node
        if not (newGameArray in nodesVisited): # Make sure node is not visited already
            newNode = Node(newGameArray, node.steps + mov + ', ')
            visitNodeIDS(newNode, depthLimit)
    depth -= 1    

def solveIDS(gameArray):
    global depth, nodesVisited
    print('Using IDS')
    root = Node(gameArray, '')
    depthLimit = 0
    while not winnerFound:
        print ('Trying Depth Limit: ' + str(depthLimit))
        visitNodeIDS(root, depthLimit)
        nodesVisited = [root]
        depthLimit += 1
        depth = 0


# Heuristic One: Number of Tiles Out of Place
# (Excluding Blank Tile)
def h1(gameArray):
    totalMisplaced = 9 - sum(np.array(gameArray) == np.array(goalState))
    if gameArray.index(0) != 4:
        totalMisplaced -= 1
    return totalMisplaced

# Heuristic Two: Sum of Manhatten Distance
def h2(gameArray):
    sum = 0
    for index,toCheck in enumerate(gameArray):
        if (toCheck == 0):
            continue
        oldRow, oldCol = int(index/3), (index % 3)
        goalIndex = goalState.index(toCheck)
        goalRow, goalCol = int(goalIndex/3), (goalIndex % 3)
        sum += abs(goalCol - oldCol) + abs(goalRow - oldRow)
    return sum

def nodeComparator(item):
    return item.fValue

# # # # # # # # # # # #
#        Greedy       #
# # # # # # # # # # # #

def expandNodeGreedy(nodeList, heuristic):
    global numNodesVisited

    numNodesVisited += 1
    theNode = nodeList.pop(0)
    movements = getPossibleMotions(theNode.gameArray)
    for mov in movements:
        newGameArray = makeMovement(list(theNode.gameArray), mov)
        newNode = NodeInformed (newGameArray, theNode.steps + mov + ', ', heuristic(newGameArray))
        nodeList.append(newNode)


def solveGreedy(gameArray, heuristic):
    root = NodeInformed(gameArray, '', heuristic(gameArray))
    nodeList = [root]
    while not winnerFound:
        # Sort Node List
        nodeList = sorted(nodeList, key=nodeComparator)
        # Check if solution
        if (nodeList[0].gameArray == goalState):
            break
        print(nodeList[0])
        print('\n')
        # Expand First Node
        expandNodeGreedy (nodeList, heuristic)

    winnerNode = nodeList[0]
    print("WINNER FOUND")
    winnerNode.steps = winnerNode.steps [:-2] # remove the last ', '
    print ('Solution: ' + winnerNode.steps)
    print ('Number of nodes visited: ' + str(numNodesVisited))
    print ('Max Node List Size: ')

# # # # # # # # # #
#      A-STAR     #
# # # # # # # # # #

def expandNodeAstar(nodeList, heuristic):
    global numNodesVisited, nodesVisited

    numNodesVisited += 1
    theNode = nodeList.pop(0)
    movements = getPossibleMotions(theNode.gameArray)
    for mov in movements:
        newGameArray = makeMovement(list(theNode.gameArray), mov)
        if newGameArray in nodesVisited:
            continue
        nodesVisited.append(newGameArray)
        newNode = NodeInformed (newGameArray, theNode.steps + mov + ', ', theNode.steps.count(',') + heuristic(newGameArray))
        nodeList.append(newNode)

def solveAStar(gameArray, heuristic):
    root = NodeInformed(gameArray, '', heuristic(gameArray))
    nodeList = [root]
    while not winnerFound:
        # Sort Node List
        nodeList = sorted(nodeList, key=nodeComparator)
        # Check if solution
        if (nodeList[0].gameArray == goalState):
            break
        # Expand First Node
        expandNodeAstar (nodeList, heuristic)

    winnerNode = nodeList[0]
    print("WINNER FOUND")
    winnerNode.steps = winnerNode.steps [:-2] # remove the last ', '
    print ('Solution: ' + winnerNode.steps)
    print ('Number of nodes visited: ' + str(numNodesVisited))
    print ('Max Node List Size: ')

# Show menu and let user choose algorithm
def chooseAlgoAndSolve (gameArray):
    print('1. DFS\n2. BFS\n3. IDS\n4. Greedy Best-First\n5. A-Star')
    choice = int(input('Enter no.: '))
    if (choice == 1):
        solveDFS(gameArray)
    elif (choice == 2):
        solveBFS(gameArray)
    elif (choice == 3):
        solveIDS(gameArray)
    elif (choice == 4):
        solveGreedy(gameArray, h1)
    elif (choice == 5):
        solveAStar(gameArray, h2)
    else:
        print ('Wrong Choice')

def inputGameArray():
    # Input the array using map
    toReturn = list(map(int, input('Please enter initial game array: ').split()))
    return toReturn

# Takes Lisp-Style input from user and executes required algorithm
def inputLispStyle():
    inputString = input('')
    # get rid of leading and ending )s
    inputString = inputString[(inputString.index('(') + 1):]
    inputString = inputString[:(inputString.index(')'))]
    algoType = inputString.split() [0]
    numbers = inputString.split('(') [1]
    gameArray = list(map(int,numbers.strip().split()))[:9]
    if (algoType == 'dfs'):
        solveDFS(gameArray)
    elif (algoType == 'bfs'):
        solveBFS(gameArray)
    elif (algoType == 'ids'):
        solveIDS(gameArray)
    elif (algoType == 'greedy'):
        solveGreedy(gameArray, h2)
    elif (algoType == 'astar'):
        solveAStar(gameArray, h1)

    

def main():
    # inputLispStyle()
    gameArray = inputGameArray()
    chooseAlgoAndSolve(gameArray)

if __name__ == '__main__':
    main()