import math

def calculateSeatId(code):
    
    # Calculate row
    upperRow = 127
    lowerRow = 0
    
    for letter in code[:7]:
      
        midrow = (upperRow - lowerRow)/2 + lowerRow
        
        if letter =='F':
            upperRow = math.floor(midrow)
            rowNumber = upperRow
            
        elif letter == 'B':
            lowerRow = math.ceil(midrow)
            rowNumber = lowerRow
    
    # Calculate seat
    upperSeat = 7
    lowerSeat = 0
    for letter in code[7:]:
        
        midseat = (upperSeat - lowerSeat)/2 + lowerSeat
        
        if letter == 'L':
            upperSeat = math.floor(midseat)
            seatNumber = upperSeat
        if letter == 'R':
            lowerSeat = math.ceil(midseat)
            seatNumber = lowerSeat
            
    seatId = rowNumber*8 + seatNumber        
    
    return (rowNumber, seatNumber)
    
file = open('input.txt', 'r').readlines()

val = 0

seatGrid = []
for i in range(127):
    seatGrid.append([0]*8)

for line in file:
    row, col = calculateSeatId(line)
    seatGrid[row][col] = 1
    

flag = False
for ridx, row in enumerate(seatGrid):
    for sidx, seat in enumerate(row):
        
        if seat == 1:
            flag = True
        
        if flag == True and seat == 0:
            print(ridx, sidx, ridx*8 + sidx)
            break
        
