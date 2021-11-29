import re

passports = open('input.txt', 'r').readlines()
    
updatedPass = []
for line in passports:

    if line != '\n':
        line = line.replace('\n', ' ')
    updatedPass.append(line)
    
stringVal = ''.join(updatedPass)
passports_to_validate = stringVal.split('\n')
                
req_codes = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  
matching = [s for s in passports_to_validate if all(xs in s for xs in req_codes)]
print('passports with required codes', len(matching))

#DataValidation
dict_pass = []
for line in matching:
    line = line.strip()
    line = line.replace(':', ' ')
    line = line.split(' ')
    dline = {line[i]: line[i+1] for i in range(0, len(line), 2)}
    dict_pass.append(dline)

# Conditions
cnt = 0
for line in dict_pass:
    questions = []
    for key, val in line.items():
        #test for byr
        if key == 'byr':
            if (len(val) == 4) and (int(val) >= 1920) and (int(val) <= 2020):
                questions.append(True)
        
        #test for iyr
        if key == 'iyr':
            if (len(val) == 4) and (int(val) >= 2010) and (int(val) <= 2020):
                questions.append(True)
        
        #test for eyr
        if key == 'eyr':
            if (len(val) == 4) and (int(val) >= 2020) and (int(val) <= 2030):
                questions.append(True)
            
        #test for hgt
        if key == 'hgt':
            if val[-2:] == 'cm':
                if float(val[:-2]) >= 150 and float(val[:-2]) <= 193:
                    questions.append(True)  
            
            elif val[-2:] == 'in':
                if float(val[:-2]) >= 59 and float(val[:-2]) <= 76:
                    questions.append(True) 

        #test for hcl
        if key == 'hcl':
            pattern = '[a-f0-9]{6}'
            
            if re.match(pattern, val[1:]):
                questions.append(True)                
        
        #testfor ecl
        if key == 'ecl':
            if val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                questions.append(True)
        
        #test for pid
        if key == 'pid':
            if len(val) == 9:
                questions.append(True)  

    if len(questions) == 7:
        cnt += 1

print('Number of valid passports', cnt)
        

    
