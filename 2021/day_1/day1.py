with open('input.txt') as f:
    data = f.readlines()

data = [float(x) for x in data]

cnt = 0
for idx, y in enumerate(data[:-1]):
    if y < data[idx + 1]:
        cnt += 1
        
print(cnt)