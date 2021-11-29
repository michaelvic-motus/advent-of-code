import numpy as np


def findAdjacent(row, col, floorPlan):
    
    maxRow, maxCol = np.shape(floorPlan)
    adjacent = []
    
      
    for idxCheck in range(8):
        for i in range(1, max(maxRow, maxCol)):
            checks = [(row, col-i),# left
                    (row, col+i),# right
                    (row+i, col),# below
                    (row-i, col),# above
                    (row-i, col-i),# left upper
                    (row-i, col+i),# right upper
                    (row+i, col+i),# right lower
                    (row+i, col-i)]# left lower  
            
            check = checks[idxCheck]

            if check[0] < 0 or check[1] < 0:
                break

            try:
                testSeat = floorPlan[check] 
                if testSeat == '#' or  testSeat == 'L':

                    #print(check, testSeat)
                    
                    adjacent.append(testSeat)
                    break
                #print(i, check)
                                
            except:
                pass
    return adjacent


def evalSeat(row, col, floorPlan):
         
    adjacent = findAdjacent(row, col, floorPlan)
    
    if floorPlan[row, col] == 'L' and adjacent.count('#') == 0:
        return '#'
    elif floorPlan[row, col] == '#' and adjacent.count('#') > 4:
        return 'L'
    elif floorPlan[row, col] == '.':
        return '.'
    else:
        return floorPlan[row, col]

#=======================================================================================================================

data = open('input.txt', 'r').read().splitlines()

#Create Array
floorPlan = []
for row in data:
    floorPlan.append(list(row))
floorPlan = np.array(floorPlan)

cnt = 0
amount = 0
change = 99
while cnt < 100 :
    
    #print('Starting new iteration')

    tempFloor = np.copy(floorPlan)        
    for iRow, row in enumerate(floorPlan):
        for iCol, col in enumerate(row):
            
            if floorPlan[iRow, iCol] != '.':
            
                seat = evalSeat(iRow, iCol, floorPlan)
                tempFloor[iRow, iCol] = seat
            
    cnt += 1

    floorPlan = np.copy(tempFloor)
    
    newAmount = np.count_nonzero(floorPlan == '#') 
    #change = amount - newAmount
    amount = newAmount
        
    
    print(cnt, amount)        
   

