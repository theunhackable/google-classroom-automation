import sys
from time import sleep
from classes_today import *
from quotes import print_random_quote
inp = sys.argv[1].upper()

if inp in classes:
    open_link(classes[inp])
elif inp == 'TODAY' or inp == '-T':
    print()
    print_random_quote()
    classes_today()
elif inp == 'HELP' or inp == '-H':
    help_menu()
elif inp == 'AUTOMATE' or inp == '-A':
    subs = find_classes()
    c = 0
    while True:
        if c == 1:
            break
        time = datetime.now().time()
        time = str(time).split(':')
        for i in subs:
            if time[0] == i[0:2] and time[1] == i[3:5]:
                open_link(classes[i[20:]])
                print('Opened' + i[20:] + 'link')
                if i == subs[-1]:
                    c = 1
                    break
                sleep(3600)
                break

else:
    print('\n' + '\t' + 'Invalid command')
    print('\n' + '\t' + 'Try class -h for help menu')