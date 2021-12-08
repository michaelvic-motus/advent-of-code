

# Read and prepare data
# ---------------------

with open('input.txt') as f:
    data = f.readlines()
data = data[0].split(',')
data = [int(x) for x in data]


# Loop over list
days = 80

for day in range(1, days + 1):
    print(day)
    appendCnt = 0
    for idx, timer in enumerate(data):
        if timer == 0:
            data[idx] = 6
            appendCnt += 1    
        else:
            data[idx] = timer - 1
        
    for newFish in range(appendCnt):
        data.append(8)

    #print('day:', day, '|', data)

print('answer', len(data))
 