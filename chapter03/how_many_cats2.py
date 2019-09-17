while True:
    number = input('How many cats do you have?')
    try:
        numCats = int(number)
        if numCats < 0:
            print("Sorry, you cannot have negative cats, try again")
            continue
        break
    except ValueError:
        print("That is not an integer")
if int(numCats) >= 4:
    print('That is a lot of cats.')
else:
    print('That is not that many cats.')
