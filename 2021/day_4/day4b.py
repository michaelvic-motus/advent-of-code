import numpy as np

def checkBoards(boards, winners):   
        
    won = []
    for idx, board in enumerate(boards):     
        if -5 in np.sum(board, axis=1) and (idx not in (winners + won)):# Check rows 
            won.append(idx) 
        elif -5 in np.sum(board, axis=0) and (idx not in (winners + won)):# Check columns  
            won.append(idx)

    return won


def playBingo(boards, numbers):
    
    # Iterate over numbers
    winners = []
    winNum = []
    for number in numbers:
        
        # Find matches
        for boardNum, board in enumerate(boards):
            if boardNum not in winners:  
                board[np.where(board == number)] = -1

        won = checkBoards(boards, winners)

        if len(won) > 0:
        
            winners  = winners + won
            winNum.append(number)
            
            
            
        if len(winners) == len(boards):
            return winners, winNum

#-------------------------------------------------------------------------------

# Read Data
with open('input.txt') as f:
    data = f.readlines()
    
dataBac = data.copy()
    
# Prepare numbers
numbers = data.pop(0)
numbers = [int(num) for num in numbers.split(',')]

# Prepare boards
boards = []
data = [row.strip() for row in data if row != '\n']
while len(data) >= 4:    
    board = [data.pop(0) for _ in range(5)]
    board = [row.replace('  ', ' ') for row in board]
    board = [row.split(' ') for row in board]
    boards.append(np.array(board, dtype=int))

# play bingo 
winners, winNums = playBingo(boards, numbers)

# Calculate score of boards
# for i, winner in enumerate(winners):  
#     board = boards[winner]
#     board[board < 0] = 0 
#     score = np.sum(np.sum(boards[winner])) * winNums[i]
#     print(score)

# Calculate score of last board
board = boards[winners[-1]]
board[board < 0] = 0 
score = np.sum(np.sum(board)) * winNums[-1]
print(score)

