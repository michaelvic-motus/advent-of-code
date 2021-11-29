 
with open('input.txt', 'r') as file:
    inputs = file.readlines()

totalLength = 0
for row in inputs:
    row = row.replace('\n', '')
    row = row.split('x')
    row = [float(dim) for dim in row]
    row = sorted(row)
    
    length = 2*row[0] + 2*row[1]
    volume = row[0]*row[1]*row[2]

    
    totalLength += (length + volume)
    
print('\n', 'total length:', totalLength)