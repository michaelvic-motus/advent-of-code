
def processBoot(instructions):


    # Process instruction list
    # ------------------------
    accumulator = 0
    pointer = 0
    pointerRec = []
    operationRec = []

    while True:
        
        operation, argument = instructions[pointer].split(' ')

        if operation == 'acc':
            instructions[pointer] = 'x 0'        
            accumulator += int(argument)
            pointer += 1
            
            if pointer >= len(instructions):
                break
            
        elif operation == 'jmp':
            instructions[pointer] = 'x 0' 
            pointer += int(argument)
            
            if pointer >= len(instructions):
                break
            
        elif operation == 'nop':
            instructions[pointer] = 'x 0' 
            pointer += 1
            
            if pointer >= len(instructions):
                break
            
        elif operation == 'x':
            break
        else:
            break
    
    return accumulator, pointer

#===============================================================================

originalInstructions = open('input.txt', 'r').read().splitlines()
operationsList = [i.split(' ')[0] for i in originalInstructions]
instructions = originalInstructions[:]

searchStart = 0
lim = 100
cnt = 0
while True and cnt < lim:
    accumulator, pointer = processBoot(instructions)

    if pointer >= len(instructions):
        print('answer is:', accumulator)
        break
        
    # find index to Swap
    idx = min(operationsList.index('jmp', searchStart), operationsList.index('nop', searchStart))
    
    # Swap
    op, arg = originalInstructions[idx].split(' ')
    instructions = originalInstructions[:]
    
    if op == 'jmp':
        instructions[idx] = 'nop' + ' ' + arg
    elif op == 'nop':
        instructions[idx] = 'jmp' + ' ' + arg
    
    searchStart = idx + 1 
    cnt += 1