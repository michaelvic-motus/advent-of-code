
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
                item = string[i:].strip()
            else:
                item = 'no other bag'
            childList.append(item)
        
        data[parent] = childList 
    return data


def findParents(child, data):
    parents = []
    for key, val in data.items():
        if child in val and key not in parents:
            parents.append(key)
    return parents

#-------------------------------------------------------------------------------

ruleSet = createData('input.txt')

#Find Parents of elements in bagset
children = ['shiny gold bag']
#del ruleSet['shiny gold bag']
glob_answer = []

for i in range(0,10000):
    imPar = []
    for child in children:
        parents = findParents(child, ruleSet)
        
        imPar.extend(parents)
        
    glob_answer.extend(imPar)
        
    children = imPar
    
print(set(glob_answer))
print(len(set(glob_answer)))    


    







    
