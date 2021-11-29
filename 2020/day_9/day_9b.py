
from itertools import combinations

data = [float(i) for i in open('input.txt', 'r').read().splitlines()]
windowLen = 25

window = data[0:windowLen]


for idx, item in enumerate(data[25:]):
    
    answers = [sum(i) for i in list(combinations(window, 2))]
    
    if item not in answers:
        print('Item', item, 'index', idx)
        break
    
    # move window
    window = window[1:]
    window.append(item)  
     



