
data = open('input.txt','r').read().splitlines()
data = sorted([int(i) for i in data])
data.insert(0, 0)
data.append(data[-1] + 3)

dataDiff = []
for idx, val in enumerate(data[0:-1]):
    dataDiff.append(data[idx + 1] - data[idx])

# Count adjacent ones
cntList = [str(val) for val in dataDiff]
cntList = ''.join(cntList).split('3')
cntList = [len(val) for val in cntList if val != '']
        
# formula
combos = 1
for idx, val in enumerate(cntList):

    term1 = max(val, 1)
    
    if val > 2:
        term2 = val - 2
    else:
        term2 = 0
        
    if val > 3:
        term3 = val - 3
    else:
        term3 = 0

    print('val:', val, 'term1:', term1, 'term2:', term2, 'Total:', term1 + term2)

    combos *= (term1 + term2 + term3)
    
print(combos)
