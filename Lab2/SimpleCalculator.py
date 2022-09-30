def showValue(item):
    if item != None:
        return item
    else:
        return ''

print('Welcome to the Simple Calculator!')
cont = True
while cont:
    userInput = ''
    display = ''
    inputs = [None, None, None]
    while userInput.strip().lower() not in ['clr', 'clear']:
        userInput = str(input('')).strip()
        if userInput in '+-*/=':
            inputs[1] = userInput
        elif userInput.isdecimal():
            if inputs[0] == None:
                inputs[0] = float(userInput)
            else:
                inputs[2] = float(userInput)
        if None not in inputs:
            if inputs[1] == '+':
                display = inputs[0] + inputs[2]
            elif inputs[1] == '-':
                display = inputs[0] - inputs[2]
            elif inputs[1] == '*':
                display = inputs[0] * inputs[2]
            elif inputs[1] == '/':
                display = inputs[0] / inputs[2]
            inputs = [display, None, None]
        else:
            display = str(showValue(inputs[0])) +' '+ str(showValue(inputs[1])) +' '+ str(showValue(inputs[2]))
        if userInput.strip().lower() not in ['clr', 'clear']:
            print('| ' + str(display).strip() + ' |')
        #if len(display.split[' ']) == 3:
            #12pass

    if input('Continue? Y/N\n').lower == 'n':
        cont = False
    display = ''