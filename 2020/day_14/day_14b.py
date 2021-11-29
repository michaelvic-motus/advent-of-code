import itertools


def applyMask(address, number, mask):
    # Takes binary address and binary mask
    
    # convert mask to list
    mask = [i for i in mask]
    
    # Find indexes of all 'X''s
    xIdx = [i for i, val in enumerate(mask) if val == 'X']

    # Convert address to list
    address = [i for i in address]
    
 
    # Apply mask without floating bits
    for idx, val in enumerate(mask):
        if mask[idx] == '1':
            address[idx] = '1'
        elif mask[idx] == 'X':
            address[idx] = 'X'
               
    # create combos from floating bits
    data = {}
    if len(xIdx) > 0:
        combos = list(itertools.product([0,1], repeat=len(xIdx)))
        for combo in combos:
            for idx, value in enumerate(combo):
                address[xIdx[idx]] = str(combo[idx])
               
            addressToAppend = ''.join(address)
            
            data[addressToAppend] = number
        return data
    else:
        return {address: number}        
    
#===============================================================================

data = open('input.txt', 'r').read().splitlines()

memory = {}
for line in data:
    
    if line[0:4] == 'mask':
        mask = line[-36:]
        
    if line[0:3] == 'mem':
        address = line[line.index('[') + 1: line.index(']')]
        number = int(line[line.index('=') + 2:])
        
        #convert address to binary
        address = str(bin(int(address)))[2:]
        address = '0'*(36 - len(address)) + address
        
        
        for key, val in applyMask(address, number, mask).items():
            memory[key] = val

#===============================================================================  

# Count all values in memory
sumVal = 0
for key, val in memory.items():
    sumVal += val
    
print(sumVal)