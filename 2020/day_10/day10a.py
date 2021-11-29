import math

data = open('sample_input.txt','r').read().splitlines()
data = [int(i) for i in data]
data.sort()

dataDiff = []

for idx, val in enumerate(data[0:-1]):
    dataDiff.append(data[idx + 1] - data[idx])
    
threes = dataDiff.count(3) + 1
ones = dataDiff.count(1) + 1

answer = threes * ones
print(answer)