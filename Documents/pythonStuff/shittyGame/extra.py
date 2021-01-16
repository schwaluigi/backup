import os

def clear():    
    if os.name == 'nt':    
        _ = os.system('cls')    
    
    else:
        _ = os.system('clear')    


def fancy_text(text):
    text = str(text)
    print('┌' + '─' * (2 + (len(text))) + '┐')
    print('│ ' + text + ' │')           
    print('└' + '─' * (2 + (len(text))) + '┘')
                

