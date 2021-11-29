
def createData(file):

    rules = open(file, 'r').readlines()

    data = {}
    for line in rules:
        parent, children = line.split('contain')
        parent = parent.strip()
        parent = parent.replace('bags', 'bag')
        children = children.replace('\n', '').replace('.','').strip()
        children = children.replace('bags', 'bag')
        
        children = children.split(',')
        childList = []
        for idx, child in enumerate(children):
            string = child.strip()
            
            if string != 'no other bag':
                i = string.find(' ')
                item = [float(string[:i].strip()), string[i:].strip()]
            childList.append(item)
        
        data[parent] = childList 
    return data

#-------------------------------------------------------------------------------

ruleSet = createData('input.txt')

#Find Parents of elements in bagset
children = ['shiny gold bag']

remainingBags = list(ruleSet.keys())
remainingBags.remove('shiny gold bag')

validColours = []
while children:

    print('starting new while loop')    
 
    parents = [] 
    for child in children: 
        
        print('children', children)

             
        for parent in ruleSet.keys():
            
            print(parent)
            
            bagList = [i[1] for i in ruleSet[parent]]  
                        
            print(bagList)
                        
            if child in bagList and parent not in parents:
                print('found parent:', parent)
                parents.append(parent)    
    
    validColours.extend(parents)
        
    for parent in parents:
        if parent in ruleSet.keys():
            ruleSet.pop(parent)  
    
    children = parents[:]

print(validColours)


    
