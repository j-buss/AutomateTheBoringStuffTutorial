def collatz(number):
    try:
        integer = int(number)
    except ValueError:
        print ('Please enter an integer')
        if integer % 2 == 0:
            return integer // 2
        else:
            return 3 * integer + 1
    except:

