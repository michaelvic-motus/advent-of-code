
questions = open('input.txt', 'r').readlines()

data = []
for line in questions:
    if line != '\n':
        line = line.replace('\n', '')
    else:
        line = line.replace('\n', ' ')
    data.append(line)
data = ''.join(data)
data = data.split(' ')

answ = []
for line in data:
    answ.append(len(set(line)))
print(sum(answ))
