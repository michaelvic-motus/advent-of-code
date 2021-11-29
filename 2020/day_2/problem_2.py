# Advent of code example 2

file = open('password_db.txt')
data = file.readlines()

psw_cnt = 0
for line in data:
    # Split data into nested list
    line = line.replace('\n', '')
    line = line.replace(': ', ' ')
    line = line.replace('-', ' ')
    line = line.split(' ')
    
    # Assign values
    lb = int(line[0])
    ub = int(line[1])
    char = line[2]
    password = line[3]
    cnt = password.count(char)
    
    # Perform password check
    if cnt >= lb and cnt <= ub:
        print(password, char, cnt, lb, ub, 'success')
        psw_cnt += 1
    else:
        print(password, char, cnt, lb, ub, 'failure')
        
        
print(psw_cnt)
        

