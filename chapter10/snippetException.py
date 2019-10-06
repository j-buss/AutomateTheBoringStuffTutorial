def testException(intInput):
    if intInput == 1:
        raise Exception('''Don't use the number: ''' + str(intInput))
    print('''Number passed to function: ''' + str(intInput))

for i in range(5):
    try:
        testException(i)
    except Exception as err:
        print('An exception happend: ' + str(err))
