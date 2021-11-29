data = open('input.txt', 'r').read().splitlines()

memory = {}
for line in data:
    if line[0:4] == 'mask':
        mask = line[-36:]
        mask = [i for i in mask]
        
    if line[0:3] == 'mem':
        address = line[line.index('[') + 1: line.index(']')]
        number = int(line[line.index('=') + 2:])
        
        #convert number to binary
        bNumber = str(bin(number))[2:]
        bNumber = '0'*(36 - len(bNumber)) + bNumber
        bNumber = [i for i in bNumber]
        
        # Apply mask
        for idx, val in enumerate(bNumber):
            
            if mask[idx] != 'X':
                bNumber[idx] = mask[idx]
        
        memory[address] = ''.join(bNumber)

# Count all values in memory
sumVal = 0
for val in memory.values():
    sumVal += int(val,2)
    
print(sumVal)