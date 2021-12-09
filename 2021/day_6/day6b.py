# Read and prepare data
# ---------------------

with open('test1_input.txt') as f:
    data = f.readlines()
data = data[0].split(',')
data = [int(x) for x in data]

# def fish(cnt, days):

#     children = 0
#     while days:
#         days -= 1
#         if cnt != 0:
#             cnt -= 1
#         elif cnt == 0:
#             cnt = 6
#             children += 1 + fish(8, days)
#     return children

# days = 80

# totalFish = 0
# for item in data:
#     children = fish(item, days)
#     print(item, children)
#     totalFish += children

# print(totalFish)

data = [3]

# Loop over list
days = 256
children = []
for day in range(1, days + 1):
    appendCnt = 0
    print(day)
    for idx, timer in enumerate(data):       
        if timer == 0:
            data[idx] = 6
            appendCnt += 1    
        else:
            data[idx] = timer - 1
        
    for newFish in range(appendCnt):
        data.append(8)

    children.append(len(data))

    #print('day:', day, '|', data)

print(children)

print('answer', len(data))
