from copy import copy, deepcopy     #For making a deepcopy of state for nodes
import timeit   #For testing
import json     #For state inputing

beg =input("Insert starting pos file name:")
fin =input("Insert goal pos file name:")
heu =int(input("Input for heuristic: \n1-number of missmatched tiles\n2-sum of distances from end position\n"))

#List of operands
listOP = [] 

#Loads our starting and finishing state from files (files generated with stateGen.py)
with open(fin + '.txt') as x:
    end = json.load(x)  
with open(beg + '.txt') as x:
    start = json.load(x)

#Gets dimensions of the puzzle
m = len(start[0])
n = len(start)

#Finds number in 2D array
def findNum(arr, num):
    for i in arr:
        try:
            j = i.index(num)
            return j, arr.index(i)
        except ValueError:
            continue
        
#Prints out the steps to get to given node
def showPath(node):
    if(node.parent):
        showPath(node.parent)
    node.showGrid()
    if node.lastOp != None:
        listOP.append(node.lastOp)

#Checks for nodes with same state in given dictionary, returns true only if f value is lower
def isIn(curr, dicti):
    try:
        for i in dicti[curr.h]:
            if curr.grid == i.grid and curr.f > i.f:
                return True
        return False
    except KeyError:
        return False

#Node object representing state of puzzle and all information needed
class node:
    def __init__(self, grid, parent, depth, lastOp = None):
        self.grid = deepcopy(grid)
        self.parent = parent
        self.depth = depth
        self.h = self.heur()
        self.f = self.depth + self.h
        self.lastOp = lastOp

    #print out current grid
    def showGrid(self):
        for i in self.grid:
            for j in i:
                print("{} ".format(j), end = "")
            print("\n", end = "")
        print("")

    #shift left
    def left(self):
        x, y = findNum(self.grid, 0)
        if x < m - 1:
            self.grid[y][x] = self.grid[y][x+1]
            self.grid[y][x+1] = 0
        else:
            return -1

    #shift right
    def right(self):
        x, y = findNum(self.grid, 0)
        if x != 0:
            self.grid[y][x] = self.grid[y][x-1]
            self.grid[y][x-1] = 0
        else:
            return -1

    #shift up
    def up(self):
        x, y = findNum(self.grid, 0)
        if y < n - 1:
            self.grid[y][x] = self.grid[y+1][x]
            self.grid[y+1][x] = 0
        else:
            return -1

    #shift down
    def down(self):
        x, y = findNum(self.grid, 0)
        if y != 0:
            self.grid[y][x] = self.grid[y-1][x]
            self.grid[y-1][x] = 0
        else:
            return -1

    #placeholder for heuristic function
    def heur(self):
        pass

    #number of stones out of place
    def heur1(self):
        diff = 0
        for i in range(0, n):
            for j in range(0, m):
                if end[i][j] != self.grid[i][j]:
                    diff = diff + 1
        return diff
    
    #sum of distances from their final place
    def heur2(self):
        diff = 0
        for i in range(0, n):
            for j in range(0, m):
                if self.grid[i][j] != 0:
                    x, y = findNum(end, self.grid[i][j])
                    diff = diff + (abs(x - j) + abs(y - i))
        return diff

#Heuristics option
if heu == 1:
    node.heur = node.heur1
else:
    node.heur = node.heur2

#A* algorhitm
def Astar():
    winFlag = 0

    #While there are nodes that need to be checked/branched
    while len(opened) > 0:
        #Find lowest f in open list and set it as curr
        curr = opened[next(iter(opened))][0]
        for i in opened:
            for j in opened[i]:
                if j.f < curr.f:
                    curr = j

        #Remove current node from open list
        opened[curr.h].pop(opened[curr.h].index(curr))
        if(len(opened[curr.h]) == 0):
            opened.pop(curr.h)

        #print(curr.depth, end=" Vytvorenych: ")
        #print(len(opened), end=" Spracovanych: ")
        #print(len(closed))

        #Branch current node without reversing operation
        #In each child we check if its goal state
        #If there is a node with same state in open/closed list with lower f value we discard child
        if curr.lastOp != "left":
            temp = node(curr.grid, curr, curr.depth + 1, "right")
            if temp.h == 0:
                showPath(temp.parent)
                winFlag = 1
                break
            if(temp.right() != -1 and isIn(temp, opened) == False and isIn(temp, closed) == False):
                try:
                    opened[temp.h].append(temp)
                except KeyError:
                    opened[temp.h] = []
                    opened[temp.h].append(temp)

        if curr.lastOp != "right":
            temp = node(curr.grid, curr, curr.depth + 1, "left")
            if temp.h == 0:
                showPath(temp.parent)
                winFlag = 1
                break
            if(temp.left() != -1 and isIn(temp, opened) == False and isIn(temp, closed) == False):
                try:
                    opened[temp.h].append(temp)
                except KeyError:
                    opened[temp.h] = []
                    opened[temp.h].append(temp)
                
        if curr.lastOp != "down":
            temp = node(curr.grid, curr, curr.depth + 1, "up")
            if temp.h == 0:
                showPath(temp.parent)
                winFlag = 1
                break
            if(temp.up() != -1 and isIn(temp, opened) == False and isIn(temp, closed) == False):
                try:
                    opened[temp.h].append(temp)
                except KeyError:
                    opened[temp.h] = []
                    opened[temp.h].append(temp)

        if curr.lastOp != "up":
            temp = node(curr.grid, curr, curr.depth + 1, "down")
            if temp.h == 0:
                showPath(temp.parent)
                winFlag = 1
                break
            if(temp.down() != -1 and isIn(temp, opened) == False and isIn(temp, closed) == False):
                try:
                    opened[temp.h].append(temp)
                except KeyError:
                    opened[temp.h] = []
                    opened[temp.h].append(temp)

        #Add current node to closed list
        try:
            closed[curr.h].append(curr)
        except KeyError:
            closed[curr.h] = []
            closed[curr.h].append(curr)

    if(winFlag == 0):
        print("No solution.")

#Main start
#Initializing dictionaries
opened = {}
closed = {}

temp = node(start, None, 0)

opened[temp.h] = []
opened[temp.h].append(temp)


startTD = timeit.default_timer()
Astar()
stop = timeit.default_timer()
print("It took {:.4f} seconds to solve the puzzle.".format(stop - startTD))
c = 0
for i in closed:
    c += len(closed[i])
print("Program processed {} nodes before reaching conclusion.".format(c))
c = 0
for i in opened:
    c += len(opened[i])
print("Program was left with {} generated nodes in queue.".format(c))
print(listOP)