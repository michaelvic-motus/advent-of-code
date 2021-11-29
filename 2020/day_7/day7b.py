
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
            else:
                item = [1, 'no other bag']
            childList.append(item)
        
        data[parent] = childList 
    return data


def dfs(tree, parent, path, numParents=1):

    # Case 1 bag already counted
    if parent in path:
        pass     
    
    else:
        path.append(parent)
        
        for child in tree[parent]:
            # Case 2 node does not have children  
            if child[1] == 'no other bag':
                return numParents           
            
            # Case 2 node has children
            else:
                numChild = numParents*child[0]
                childValues = dfs(tree, child[1], path, numChild)
                
                if childValues == None:                
                    counter = numParents
                else:
                    counter = numParents + childValues 
          
        return counter
    

#===============================================================================

ruleSet = createData('sample_input_2.txt')
startNode = 'shiny gold bag'

path = []
amounts = []
amount = dfs(ruleSet, 'shiny gold bag', path)

print('total amount of bags:', amount)