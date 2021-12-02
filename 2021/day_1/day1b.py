with open('input.txt') as f:
    data = f.readlines()

data = [float(x) for x in data]

idx = 0
windowSum = []
while idx < 2000 - 2:
    windowSum.append(data[idx] + data[idx + 1] + data[idx + 2])
    idx += 1

cnt = 0
for idx, y in enumerate(windowSum[:-1]):
    if y < windowSum[idx + 1]:
        cnt += 1
    
        
print(cnt)