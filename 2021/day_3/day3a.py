import numpy as np

with open('input.txt') as f:
    data = f.readlines()
    


dataList = []

for item in data:
    item = item.replace('\n', '')
    dataList.append([int(x) for x in item])
    

    
dataArr = np.array(dataList)  


sumCols = dataArr.sum(axis=0)
entryCount = len(dataArr)

gamma = []
epsilon = []
for val in sumCols:
    if val > (entryCount - val):
        gamma.append(1)
        epsilon.append(0)
    elif val < (entryCount - val):
        gamma.append(0)
        epsilon.append(1)
        
print(gamma)

gammaDec = eval('0b' +''.join([str(x) for x in gamma]))
epsilonDec = eval('0b' +''.join([str(x) for x in epsilon]))

print(gammaDec)
print(epsilonDec)

print('Answer:', str(gammaDec * epsilonDec))
    
    