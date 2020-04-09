# MadLib (version 1)

while True:
    name = input('Enter a name: ')
    verb = input('Enter a verb: ')
    adjective = input('Enter an adjective: ')
    noun = input('Enter a noun: ')
    
    sentence = name + ' ' + verb + ' down the hill, hoping to escape the ' + \
                     adjective + ' ' + noun + '.'
    print()
    print(sentence)
    print()
    
    # See if the user wants to quit or continue
    answer = input('Type "q" to quit, or anything else (even Return/Enter) to continue: ')
    if answer == 'q':
        break

print('Bye')
