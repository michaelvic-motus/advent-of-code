instructions = open('input.txt', 'r').read().splitlines()

# Process instruction list
# ------------------------
accumulator = 0
pointer = 0


while True:
    
    operation, argument = instructions[pointer].split(' ')

    if operation == 'acc':
        instructions[pointer] = 'x 0'        
        accumulator += int(argument)
        pointer += 1
        
    elif operation == 'jmp':
        instructions[pointer] = 0     
        pointer += int(argument)
        
    elif operation == 'nop':
        instructions[pointer] = 0     
        pointer += 1
    
    elif operation == 'x':
        print(accumulator)
        break
     
    else:
        print('Invalid operation')
        break
    

    
    
    
    