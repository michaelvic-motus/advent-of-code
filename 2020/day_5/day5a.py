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
    
    print('rowNumber', rowNumber, 'seatNumber', seatNumber, 'seatId', seatId)

    return seatId     
    
file = open('input.txt', 'r').readlines()

val = 0
for line in file:
    seatId = calculateSeatId(line)

    if seatId > val: # here you could use the walruss
        val = seatId

print(val)



