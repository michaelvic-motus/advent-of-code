

# Run problem
# -----------

# Create board
with open('input.txt') as f:
    data = f.readlines()
dataNew = []
for row in data:
    row = [x for x in row.strip()]
    dataNew.append(row)
data = dataNew

faults = []
newData = []
for irow, row in enumerate(data):
    clean = True
    stack = []
    for item in row:  
              
        stackEnd = ''
        if len(stack) > 0:
            stackEnd = stack[-1]   
        openDel = ['(', '[', '{', '<']       
        closedDel = [')', ']', '}', '>']
        if item in openDel:
            stack.append(item)
        elif item in closedDel:
            idx = closedDel.index(item)
            if stack[-1] == openDel[idx]:
                stack.pop()
            else:
               faults.append(item)
               clean = False
               break
    if clean:
        newData.append(row)

                                
# Complete rows
completions = []
for row in newData:
    stack = []
    for item in row:  
        openDel = ['(', '[', '{', '<']       
        closedDel = [')', ']', '}', '>']
        if item in openDel:
            stack.append(item)
        elif item in closedDel:
            idx = closedDel.index(item)
            if stack[-1] == openDel[idx]:
                stack.pop()
    completions.append(stack)
                
# Transform completions
transfComp = []
for row in completions:
    transfRow = []
    stack = row.copy()
    for i in range(len(row)):
        idx = openDel.index(stack.pop())
        transfRow.append(closedDel[idx])
    transfComp.append(transfRow)




# Calculate score:
scoreTable = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4}

scoreList = []
for row in transfComp:
    score = 0
    for item in row:
        score = score * 5
        score += scoreTable[item]
    scoreList.append(score)
    
scoreList.sort()

mid = int(len(scoreList)/2)
score = scoreList[mid]

print(scoreList[mid])

