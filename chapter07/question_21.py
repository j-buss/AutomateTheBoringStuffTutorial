import re

def findNakamota(testString):
    personNakamota = re.compile(r'^[A-Z][a-z]+ Nakamoto$')
    mo = personNakamota.search(testString)
    try:
        print('''A proper "Nakamota" name: ''' + mo.group() + ''' was found in: ''' + testString)
    except:
        print('''--------''' + testString + ''' doesn't have a proper "Nakamota" name''')

def main():
    testlist = ['Satoshi Nakamoto', 'Alice Nakamoto', 'Robocop Nakamoto',
            'satoshi Nakamoto','Mr. Nakamoto','Nakamoto','Satoshi nakamoto']
    for n in testlist:
        findNakamota(n)

if __name__ == "__main__":
    main()
