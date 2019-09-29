import re

def findThreeDigitCommas(testString):
    threeDigitCommas = re.compile(r'^\d{1,3}(,\d{3})*$')
    mo = threeDigitCommas.search(testString)
    try:
        print('''The "three Digit Comma" number: ''' + mo.group() + ''' was found in: ''' + testString)
    except:
        print('''--------''' + testString + ''' doesn't have a "three Digit Comma" number''')

def main():
    testlist = ['42', '1,234', '1234','6,368,745','12,34,567','1234']
    for n in testlist:
        findThreeDigitCommas(n)

if __name__ == "__main__":
    main()
