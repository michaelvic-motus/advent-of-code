questions = open('input.txt', 'r').readlines()

data = []
for line in questions:
    if line != '\n':
        line = line.replace('\n', ':')
    else:
        line = line.replace('\n', ' ')
    data.append(line)
data = ''.join(data)
data = data.split(' ')

procData = []
answer = 0
for line in data:
    line = line[:-1]
    numPeople = line.count(':') + 1
    answs = set(''.join(line.replace(':',''))) 

    for ans in answs:
        if line.count(ans) == numPeople:
            answer += 1
            
print('Answer:', answer)
