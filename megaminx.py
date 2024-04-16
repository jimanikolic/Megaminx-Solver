#CS463G - UKY
#Megaminx Representation Project


#This model is based off of https://www.grubiks.com/puzzles/megaminx-3x3x3/
#In this representation, white is on top and juniper faces forwards
#Each color and face is listed from top to bottom, clockwise, counting up

#dictonary representing all adjacent sides

import random as rand
import math
import heapq
import copy
import time

#Print faces w and s
def printEnds(megaminx, facenum) :
    print('                                                     ',megaminx[facenum][1])
    print('                                                ',megaminx[facenum][10],'       ',megaminx[facenum][2])
    print('                                             ',megaminx[facenum][9],'     ',megaminx[facenum][0],'     ',megaminx[facenum][3])
    print('                                               ',megaminx[facenum][8],'         ',megaminx[facenum][4])
    print('                                                 ', megaminx[facenum][7],' ', megaminx[facenum][6],' ',megaminx[facenum][5])
    print()

#Print faces on the bottom row
def printBottomRow(megaminx, facenum) :

    print('                   ',megaminx[facenum][1],'       ','            ',megaminx[facenum+1][1],'       ','            ',megaminx[facenum+2][1],'       ','            ',megaminx[facenum+3][1],'       ','            ',megaminx[facenum+4][1],'       ')
    print('              ',megaminx[facenum][10],'       ',megaminx[facenum][2],'          ',megaminx[facenum+1][10],'       ',megaminx[facenum+1][2],'          ',megaminx[facenum+2][10],'       ',megaminx[facenum+2][2],'          ',megaminx[facenum+3][10],'       ',megaminx[facenum+3][2],'          ',megaminx[facenum+4][10],'       ',megaminx[facenum+4][2])
    print('           ',megaminx[facenum][9],'     ',megaminx[facenum][0],'     ',megaminx[facenum][3],'    ',megaminx[facenum+1][9],'     ',megaminx[facenum+1][0],'     ',megaminx[facenum+1][3],'    ',megaminx[facenum+2][9],'     ',megaminx[facenum+2][0],'     ',megaminx[facenum+2][3],'    ',megaminx[facenum+3][9],'     ',megaminx[facenum+3][0],'     ',megaminx[facenum+3][3],'    ',megaminx[facenum+4][9],'     ',megaminx[facenum+4][0],'     ',megaminx[facenum+4][3])
    print('             ',megaminx[facenum][8],'         ',megaminx[facenum][4],'        ',megaminx[facenum+1][8],'         ',megaminx[facenum+1][4],'        ',megaminx[facenum+2][8],'         ',megaminx[facenum+2][4],'        ',megaminx[facenum+3][8],'         ',megaminx[facenum+3][4],'        ',megaminx[facenum+4][8],'         ',megaminx[facenum+4][4])
    print('               ', megaminx[facenum][7],' ', megaminx[facenum][6],' ',megaminx[facenum][5],'            ', megaminx[facenum+1][7],' ', megaminx[facenum+1][6],' ',megaminx[facenum+1][5],'            ', megaminx[facenum+2][7],' ', megaminx[facenum+2][6],' ',megaminx[facenum+2][5],'            ', megaminx[facenum+3][7],' ', megaminx[facenum+3][6],' ',megaminx[facenum+3][5],'            ', megaminx[facenum+4][7],' ', megaminx[facenum+4][6],' ',megaminx[facenum+4][5])

#Print faces on the top row
def printTopRow(megaminx, facenum) :
    print('   ', megaminx[facenum][5],' ', megaminx[facenum][6],' ',megaminx[facenum][7],'            ', megaminx[facenum+1][5],' ', megaminx[facenum+1][6],' ',megaminx[facenum+1][7],'            ', megaminx[facenum+2][5],' ', megaminx[facenum+2][6],' ',megaminx[facenum+2][7],'            ', megaminx[facenum+3][5],' ', megaminx[facenum+3][6],' ',megaminx[facenum+3][7],'            ', megaminx[facenum+4][5],' ', megaminx[facenum+4][6],' ',megaminx[facenum+4][7])
    print(' ',megaminx[facenum][4],'         ',megaminx[facenum][8],'        ',megaminx[facenum+1][4],'         ',megaminx[facenum+1][8],'        ',megaminx[facenum+2][4],'         ',megaminx[facenum+2][8],'        ',megaminx[facenum+3][4],'         ',megaminx[facenum+3][8],'        ',megaminx[facenum+4][4],'         ',megaminx[facenum+4][8],)
    print(megaminx[facenum][3],'     ',megaminx[facenum][0],'     ',megaminx[facenum][9],'    ',megaminx[facenum+1][3],'     ',megaminx[facenum+1][0],'     ',megaminx[facenum+1][9],'    ',megaminx[facenum+2][3],'     ',megaminx[facenum+2][0],'     ',megaminx[facenum+2][9],'    ',megaminx[facenum+3][3],'     ',megaminx[facenum+3][0],'     ',megaminx[facenum+3][9],'    ',megaminx[facenum+4][3],'     ',megaminx[facenum+4][0],'     ',megaminx[facenum+4][9])
    print('  ',megaminx[facenum][2],'       ',megaminx[facenum][10],'          ',megaminx[facenum+1][2],'       ',megaminx[facenum+1][10],'          ',megaminx[facenum+2][2],'       ',megaminx[facenum+2][10],'          ',megaminx[facenum+3][2],'       ',megaminx[facenum+3][10],'          ',megaminx[facenum+4][2],'       ',megaminx[facenum+4][10])
    print('       ',megaminx[facenum][1],'       ','            ',megaminx[facenum+1][1],'       ','            ',megaminx[facenum+2][1],'       ','            ',megaminx[facenum+3][1],'       ','            ',megaminx[facenum+4][1],'       ')

#Utilize the above print functions to print a complete megaminx
def printMegaminx(megaminx) :
    printEnds(megaminx, 0)
    printTopRow(megaminx, 1)
    printBottomRow(megaminx, 6)
    printEnds(megaminx, 11)

#Passes in two faces adjacent to the rotated face, and three of their cubees to be swapped.
def swapAdjacent(megaminx, faceColor, adj1, cubee1, cubee2, cubee3, adj2, cubee4,cubee5,cubee6):
    megaminx[colors.index(adjacents[faceColor][adj1])][cubee1], megaminx[colors.index(adjacents[faceColor][adj1])][cubee2], megaminx[colors.index(adjacents[faceColor][adj1])][cubee3] = megaminx[colors.index(adjacents[faceColor][adj2])][cubee4], megaminx[colors.index(adjacents[faceColor][adj2])][cubee5],megaminx[colors.index(adjacents[faceColor][adj2])][cubee6]

#Moves each 
def cycleCubees(megaminx, face):
#Three cubees changes at a time, need to store 3, cycle cubees clockwise
    temp1 = megaminx[face][1]
    temp2 = megaminx[face][2]
    temp3 = megaminx[face][3]
    megaminx[face][1], megaminx[face][2],megaminx[face][3] = megaminx[face][9], megaminx[face][10], temp1
    megaminx[face][9], megaminx[face][10] = megaminx[face][7], megaminx[face][8]
    megaminx[face][7], megaminx[face][8] = megaminx[face][5], megaminx[face][6]
    megaminx[face][5], megaminx[face][6] = temp3, megaminx[face][4]
    megaminx[face][4] = temp2

#Moves a specified face clockwise
def moveFaceClockwise(megaminx, face):
    faceColor = colors[face]  #number index of the random color

    #The system I have implemented to number sides and cubees is different for the tops and bottoms, w and s.
    if faceColor != 'w' and faceColor != 's':
        temp1 = megaminx[colors.index(adjacents[faceColor][1])][1]
        temp2 = megaminx[colors.index(adjacents[faceColor][1])][2]
        temp3 = megaminx[colors.index(adjacents[faceColor][1])][3]
        #The following convention is used in this code:
        #Top left adjacent face = 0
        #Top right adjacent face = 1
        #Bottom right adjacent face = 2
        #Bottom middle face = 3
        #Bottom left face = 4
        #Each swapAdjacent moves corresponding to the previous, together cycling each adjacent face cubees, equaling one turn

        #Swap face 1 adjacent edge cubees with adjacent face 0 edge cubees
        swapAdjacent(megaminx, faceColor,1,1,2,3,0,9,10,1)

        #Swap face 0 adjacent edge cubees with adjacent face 4 edge cubees
        swapAdjacent(megaminx,faceColor,0,9,10,1,4,3,4,5)

        #Each face in relation to the top or bottom will swap a different set of cubees as determined by the top and bottom faces
        #y and t are top right of white and silver respectively or position 0
        if faceColor == 'y' or faceColor == 't':
            swapAdjacent(megaminx, faceColor,4,3,4,5,3,9,10,1)
            swapAdjacent(megaminx,faceColor,3,9,10,1,2,7,8,9)
        #b and l are top right of white and silver respectively or position 1
        elif faceColor =='b' or faceColor == 'l':
            swapAdjacent(megaminx,faceColor,4,3,4,5,3,1,2,3)
            swapAdjacent(megaminx,faceColor,3,1,2,3,2,7,8,9)
        #r and p are bottom right of white and silver respectively or position 2
        elif faceColor =='r' or faceColor == 'm':
            swapAdjacent(megaminx,faceColor,4,3,4,5,3,3,4,5)
            swapAdjacent(megaminx,faceColor,3,3,4,5,2,7,8,9)
        #r and p are bottom of white and silver respectively or position 3
        elif faceColor =='j' or faceColor == 'g':
            swapAdjacent(megaminx,faceColor,4,3,4,5,3,5,6,7)
            swapAdjacent(megaminx,faceColor,3,5,6,7,2,7,8,9)
        #r and p are bottom left of white and silver respectively or position 4
        elif faceColor =='p' or faceColor == 'o':
            swapAdjacent(megaminx,faceColor,4,3,4,5,3,7,8,9)
            swapAdjacent(megaminx,faceColor,3,7,8,9,2,7,8,9)

        #Use temps from adjacent in spot 1, top right, to fill in missing values for face 2, completing the cycle
        megaminx[colors.index(adjacents[faceColor][2])][7] = temp1
        megaminx[colors.index(adjacents[faceColor][2])][8] = temp2
        megaminx[colors.index(adjacents[faceColor][2])][9] = temp3
   
    #Completing the remaining cases for rotating faces, top and bottom, w and s, are the same
    #This is the same process as before however, numberal indexes change
    if faceColor == 'w' or faceColor == 's':
        temp1 = megaminx[colors.index(adjacents[faceColor][1])][5]
        temp2 = megaminx[colors.index(adjacents[faceColor][1])][6]
        temp3 = megaminx[colors.index(adjacents[faceColor][1])][7]

        #Swap face 1 adjacent edge cubees with adjacent face 0 edge cubees
        swapAdjacent(megaminx, faceColor,1,5,6,7,0,5,6,7)
        #Swap face 0 adjacent edge cubees with adjacent face 4 edge cubees
        swapAdjacent(megaminx, faceColor,0,5,6,7,4,5,6,7)
        #Swap face 4 adjacent edge cubees with adjacent face 3 edge cubees
        swapAdjacent(megaminx, faceColor,4,5,6,7,3,5,6,7)
        #Swap face 3 adjacent edge cubees with adjacent face 2 edge cubees
        swapAdjacent(megaminx, faceColor,3,5,6,7,2,5,6,7)

        #Use temps from adjacent in spot 1, top right, to fill in missing values for face 2, completing the cycle
        megaminx[colors.index(adjacents[faceColor][2])][5] = temp1
        megaminx[colors.index(adjacents[faceColor][2])][6] = temp2
        megaminx[colors.index(adjacents[faceColor][2])][7] = temp3

    #Cycle the cubees in the rotated face
    cycleCubees(megaminx, face)

#Equivalent to 4 clockwise moves
def moveFaceCounterClockwise(megaminx, face):
    for i in range (0,4):
        moveFaceClockwise(megaminx, face)

#Given a int shuffles, randomizes a cube
def randomize(megaminx, shuffles):
    for i in range (0, shuffles):
        #Randomize which face will be rotated
        face = rand.randint(0,11)
        moveFaceClockwise(megaminx, face)
        #print("Moved", faceColor, 'Clockwise: ')
 
#Generate the heuristic based on the number of stickers out of place
def genHeuristic(mixedMinx):
    numPieces = 0
    for i in range (12):
        for j in range(1,11):
            if mixedMinx[i][0] != mixedMinx[i][j]:
                numPieces = numPieces + 1
    numPieces = numPieces/15
    heuristic = math.ceil(numPieces)

    return heuristic

#Check if mixed state has been solved
def isSolved(mixedMinx, solvedMinx):
    if mixedMinx == solvedMinx:
        return True
    else:
        return False

#A star function, given the mixed state and the solved state
def aStar(mixedMinx, solvedMinx):

    openSet = []  # Priority queue for states to explor4e
    closedSet = set()
    #Initialize the heap to store the possible states
    heapq.heappush(openSet,(genHeuristic(mixedMinx), mixedMinx , 0 ))
    g = 0
    increment = 0

    #While no solution has been found YET and a solution may exist
    while openSet:
        _, current_state, cost = heapq.heappop(openSet)
        #Node counter
        increment += 1
        if isSolved(current_state, solvedMinx):
            printMegaminx(current_state)
            endTime = time.time()
            return endTime
       #Add node to explored
        closedSet.add(tuple(map(tuple, current_state)))

        g = cost + 1 
        #Make a move for each face, store them in the heap with their heuristic value
        for i in range(12):
            successor_state = copy.deepcopy(current_state)
            moveFaceCounterClockwise(successor_state, i)
            if (tuple(map(tuple, successor_state))) not in closedSet:
                f = g + genHeuristic(successor_state)
                heapq.heappush(openSet, (f, successor_state, g))
   

    #If the open_set becomes empty, no solution was found
    return None

adjacents = {
    'w' : ['y','b','r','j','p'],
    'j' : ['l','t','p','w','r'],
    'p' : ['t','o','y','w','j'],
    'y' : ['o','g','b','w','p'],
    'b' : ['g','m','r','w','y'],
    'r' : ['m','l','j','w','b'],
    't' : ['p','j','l','s','o'],
    'o' : ['y','p','t','s','g'],
    'g' : ['b','y','o','s','m'],
    'm' : ['r','b','g','s','l'],
    'l' : ['j','r','m','s','t'],
    's' : ['t','l','m','g','o']
}

#All colors from all 12 faces present
#white, juniper, purple, yellow , blue, red, teal, orange, green, magenta, lemon, silver
colors = ['w', 'j', 'p', 'y', 'b', 'r', 't', 'o', 'g', 'm', 'l', 's']

def main():
    #Initialize the solved minx
    solvedMinx = [[0 for i in range(11)] for j in range(12)]
    for i in range(12):
        for j in range (11):
            solvedMinx[i][j] = colors[i]

    #Shuffles 5 megaminxes x amount of times each, x in range 3-11
    for i in range (3,11):
        for n in range (5):
            
            megaminx = [[0 for j in range(11)] for k in range(12)]

            #Recreate megamix each time
            for j in range(12):
                for k in range (11):
                    megaminx[j][k] = colors[j]

            startTime = time.time()
            shuffles = i
            randomize(megaminx, shuffles)
            endTime = aStar(megaminx, solvedMinx)
            #time.sleep(3)
            print("Time elapsed to solve",i,"was:",endTime - startTime)
            

if __name__ == "__main__":
    main()
