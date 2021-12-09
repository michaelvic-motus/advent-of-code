
# Recursive call
def fish(daysLeft, timer, dataTable):
    
    #TODO: add lookup table with finished values
    
    children = 1
    for day in range(1, daysLeft + 1):    
        # Base Case
        if (timer <= 8) and (daysLeft <= 8):
            return 1
        # General Case
        if timer == 0:
            timer = 6
            children += fish(daysLeft - day, 8, dataTable)           
        else:
            timer -= 1    
    return children

# Read and prepare data
# ---------------------
with open('input.txt') as f:
    data = f.readlines()
data = data[0].split(',')
data = [int(x) for x in data]

#TODO: Add lookup table

totalChildren = 0
daysLeft = 256
dataTable = {}
for entry in data:   
    children = fish(daysLeft, entry, dataTable) 
    totalChildren += children  
print(totalChildren)

 
