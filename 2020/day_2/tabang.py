import pandas as pd							
 
# read csv data 
file = pd.read_csv('criterialist.csv', header = None)			#could have done this with a file input = 'criterialist.txt',with open(file_input, 'r') as file

counter = 0

for i in file[0]:

    a = i.split(":")
    password = a.pop().strip()
    
    b = a.pop().split(" ")
    letter = b.pop()
    c = b.pop().split("-")
    pos2 = int(c.pop())
    pos1 = int(c.pop())
   
    
    if password[pos1-1] == letter or password[pos2-1] == letter:
        counter = counter + 1
print (counter)