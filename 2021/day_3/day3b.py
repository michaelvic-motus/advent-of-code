
def findCommon(listOfLists):
    
    valCount = [0] * len(listOfLists[0])
    for row in listOfLists:
        for idx, val in enumerate(row):
            valCount[idx] += val

    nrows = len(listOfLists)

    mostCommon = []
    for val in valCount:
        if val >= (nrows - val):
            mostCommon.append(1)
        elif val < (nrows - val):
            mostCommon.append(0)
                            
    return mostCommon

def findUnCommon(listOfLists):
    
    valCount = [0] * len(listOfLists[0])
    for row in listOfLists:
        for idx, val in enumerate(row):
            valCount[idx] += val

    nrows = len(listOfLists)
    mostUnCommon = []
    for val in valCount:
        if val >= (nrows - val):
            mostUnCommon.append(0)
        elif val < (nrows - val):
            mostUnCommon.append(1)
                            
    return mostUnCommon

#-------------------------------------------------------------------------------

with open('input.txt') as f:
    data = f.readlines()

codeList = []
for item in data:
    item = item.replace('\n', '')
    codeList.append([int(x) for x in item])
 
# Oxygen -> most common    
# ---------------------   
ox = codeList.copy()
codeLength = len(codeList[0])
for i in range(codeLength):  
    mostCommon = findCommon(ox)
    
    delList = []
    for j, code in enumerate(ox):
        if code[i] != mostCommon[i]:
            delList.append(j)
    
    oxNew = [code for idx, code in enumerate(ox) if idx not in delList]
    ox = oxNew.copy()
    

# CO2 Least common    #! Issue is here
# ----------------
co2 = codeList.copy()
codeLength = len(codeList[0])
for i in range(codeLength):  
    
    if len(co2) <= 1:
        break
    
    print(co2)
    
    mostUnCommon = findUnCommon(co2)
    
    print('most uncommon:', mostUnCommon[i])
    
    delList = []
    for j, code in enumerate(co2):
        
        print('comparrison:', code[i], mostUnCommon[i], j)
        
        if code[i] != mostUnCommon[i]:
            delList.append(j)
    
    print('delList:', delList)
    co2New = [code for idx, code in enumerate(co2) if idx not in delList]
    co2 = co2New.copy()
    
# Calculate results
# -----------------
oxDec = eval('0b' + ''.join([str(x) for x in ox[0]]))
co2Dec = eval('0b' + ''.join([str(x) for x in co2[0]]))

print('oxDec:', oxDec)
print('co2Dec:', co2Dec)


print('Answer:', str(oxDec * co2Dec))
    
    