import networkx as nx

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
            
            if string != 'no other bag':
                i = string.find(' ')
                item = [float(string[:i].strip()), string[i:].strip()]
            childList.append(item)
        
        data[parent] = childList 
    return data

#-------------------------------------------------------------------------------

data = createData('input.txt')

G = nx.DiGraph()
for key, val in data.items():
    for node in val:
        G.add_edge(key, node[1])