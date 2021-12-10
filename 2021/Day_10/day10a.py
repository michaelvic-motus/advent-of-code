
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
for row in data:
    print(row)
    stack = []
    for item in row:  
              
        stackEnd = ''
        if len(stack) > 0:
            stackEnd = stack[-1]
            
        print(stackEnd, item)
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
               break
                                
print(faults)

# Calculate score:
scoreTable = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137}

score = 0
for item in faults:
    score += scoreTable[item]

print(score)
