
from itertools import combinations

data = [float(i) for i in open('input.txt', 'r').read().splitlines()]
windowLen = 25

window = data#data[484-25:484]

num = 27911108


for idx, root in enumerate(window[:-2]):
    upperBound = len(data) - idx
    
    for end in range(2, upperBound+1):
        test = window[idx:idx+end]

        answer = int(sum(test))        
        if num == answer:
            print('found combo')
            combo = test
            combo.sort()
            encriptWeak = combo[0] + combo[-1]
            print(int(encriptWeak))
            
        



