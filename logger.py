with open('log.txt', 'r+') as log:
    count = len([timestamp for timestamp in log if timestamp.startswith('[')])
    print(f'{count} exceptions stored in log')
    if count > 0:
        clear = input('Clear file? (y/n) ')
        if clear.upper() == 'Y':
            log.truncate(0)