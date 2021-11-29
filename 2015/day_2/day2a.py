 
with open('input.txt', 'r') as file:
    inputs = file.readlines()

totalArea = 0
for row in inputs:
    row = row.replace('\n', '')
    row = row.split('x')
    row = [float(dim) for dim in row]
    row = sorted(row)
    
    area = 3*row[0]*row[1] + 2*row[1]*row[2] + 2*row[0]*row[2]
    
    print(row, area)
    
    totalArea += area
    
print('\n', 'total area:', totalArea)
    
    