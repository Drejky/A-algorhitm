from copy import copy, deepcopy
import timeit
import random
import json
import bisect

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

def isIn(curr, arr):
    for i in arr:
        if curr.grid == i.grid and curr.f > i.f:
            return True
    return False

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
                print("{}, ".format(j), end = "")
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
                    #print("{} {}".format(self.grid[i][j],abs(x - j) + abs(y - i)))
        return diff

#Heuristics option
if heu == 1:
    node.heur = node.heur1
else:
    node.heur = node.heur2

#A* algorhitm
def Astar():
    while len(opened) > 0:
        curr = opened[0]
        for i in opened:
            if i.f < curr.f:
                curr = i

        opened.pop(opened.index(curr))

        print(curr.depth, end=" Vytvorenych: ")
        print(len(opened), end=" Spracovanych: ")
        print(len(closed))

        if curr.h == 0:
            print(curr.grid)
            showPath(curr.parent)
            break
        else:
            if curr.lastOp != "left":
                temp = node(curr.grid, curr, curr.depth + 1, "right")
                if(temp.right() != -1 and isIn(temp, opened) == False and isIn(temp, closed) == False):
                    opened.append(temp)

            if curr.lastOp != "right":
                temp = node(curr.grid, curr, curr.depth + 1, "left")
                if(temp.left() != -1 and isIn(temp, opened) == False and isIn(temp, closed) == False):
                    opened.append(temp)
                    
            if curr.lastOp != "down":
                temp = node(curr.grid, curr, curr.depth + 1, "up")
                if(temp.up() != -1 and isIn(temp, opened) == False and isIn(temp, closed) == False):
                    opened.append(temp)

            if curr.lastOp != "up":
                temp = node(curr.grid, curr, curr.depth + 1, "down")
                if(temp.down() != -1 and isIn(temp, opened) == False and isIn(temp, closed) == False):
                    opened.append(temp)

        closed.append(curr)

#Main start
#Initializing dictionaries
opened = []
closed = []

opened.append(node(start, None, 0))

startTD = timeit.default_timer()
Astar()
stop = timeit.default_timer()
print("It took {:.4f} seconds to solve the puzzle.".format(stop - startTD))
print(listOP)
