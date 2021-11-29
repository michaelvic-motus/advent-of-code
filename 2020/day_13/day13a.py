timestamp, data = open('input.txt', 'r').read().splitlines()

data = sorted([int(val) for val in data.split(',') if val != 'x'])

#Find starting location
nextArrivalList = []
for bus in data:
    prevArrival = int(timestamp) - int(timestamp)%bus 
    nextArrival = prevArrival + bus
    nextArrivalList.append(nextArrival)
    
nextArrivalTime = [val - int(timestamp) for val in nextArrivalList]
