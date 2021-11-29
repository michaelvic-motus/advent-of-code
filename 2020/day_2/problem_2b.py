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
    
    # Perform password check
    if (password[lb - 1] == char) and (password[ub - 1] == char):
        print(password, char, lb, ub, 'failure both positions')
        
    elif (password[lb - 1] != char) and (password[ub - 1] != char):
        print(password, char, lb, ub, 'failure no positions')
    
    else:
        print(password, char, lb, ub, 'success')
        psw_cnt += 1     
        
print('\n', 'Number of valid passwords:', psw_cnt)