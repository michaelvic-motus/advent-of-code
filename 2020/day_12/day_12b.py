
def retDir(currentDir, rotation):   
   
    rotDir = rotation[0]
    rotVal = int(rotation[1:])/90
    
    print(rotDir)
    print(rotVal)
    
    directions = ['N', 'E', 'S', 'W']
    dirIdx = directions.index(currentDir)
      
    if rotation[0] == 'R':
        diffRot = rotVal
    elif rotation[0] == 'L':
        diffRot = -rotVal
        

    
    dirIdx = int((dirIdx + diffRot)%len(directions))
    
    print(dirIdx)

    retVal = directions[dirIdx]

    return retVal   

#===============================================================================

# assume start at (0, 0)

data = open('input.txt', 'r').read().splitlines()

vector = [[], []]
currentDir = 'E'
for i, val in enumerate(data):
    
    # Change direction
    if val[0] == 'R' or val[0] == 'L':
                
        currentDir = retDir(currentDir, val)
  
    else:
        if val[0] == 'F':
            val = currentDir + val[1:]
            
        #print(val)
             
        if val[0] == 'E':
            vector[0].append(float(val[1:]))
        
        elif val[0] == 'W':
            vector[0].append(-float(val[1:]))

        elif val[0] == 'N':
            vector[1].append(float(val[1:]))

        elif val[0] == 'S':
            vector[1].append(-float(val[1:])) 


answer = (sum(vector[0]), sum(vector[1]))

print(sum([abs(val) for val in answer]))