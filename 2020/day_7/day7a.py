
def createData(file):

    rules = open('input.txt', 'r').readlines()

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
            
            if string == 'no other bag':
                item = 0
            else:
                i = string.find(' ')
                item = [float(string[:i].strip()), string[i:].strip()]
            childList.append(item)
        
        data[parent] = childList 
    
    return data

def findParents(data, child):

    bags = []
    for key, val in data.items():
        
        searchList = []
        if val != [0]:
            for num, item in val:
                if child in item:
                    searchList.append(True)
            
            if any(searchList):
                bags.append(key) 
                
    return set(bags)

#-------------------------------------------------------------------------------

data = createData('input.txt')

#TODO: handle both bags and bag, loop over and clean maybe in read function

#Find Parents of elements

bagSet = set(['shiny gold bag'])
cond = True
length = len(bagSet)

while cond: 
  
    for i in bagSet:
        
        print('bagset', bagSet)
        
        print(i)# Child
               
        addedBagSet = findParents(data, i)
        
        print(addedBagSet)# Parents
       
        newBagSet = bagSet.copy()

        for element in addedBagSet:
            newBagSet.add(element)
            
    bagSet = newBagSet.copy()
        
    if length == len(bagSet):
        cond = False
    length = len(bagSet)
    
bagSet.remove('shiny gold bag')