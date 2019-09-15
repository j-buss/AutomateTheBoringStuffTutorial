continue_flag = 'Y'
while continue_flag == 'Y':
    print('Please enter a value for spam')
    spam = input()
    if spam == '1':
        print('Hello')
    elif spam == '2':
        print('Howdy')
    else:
        print('Greetings!')
    print('Continue? (Y for YES, Anything else is NO)')
    continue_flag = input()
