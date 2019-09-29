import re

def aliceEatsApples(testString):
    #aliceEatsApples = re.compile(r'^(alice|bob|carol) (eats|pets|throws) (apples|cats|baseballs)$', re.IGNORECASE)
    aliceEatsApples = re.compile(r'^(alice|bob|carol) (eats|pets|throws) (apples|cats|baseballs).$', re.IGNORECASE)
    mo = aliceEatsApples.search(testString)
    try:
        print('''A proper "Alice eats apples." sentence: ''' + mo.group() + ''' was found in: ''' + testString)
    except:
        print('''--------''' + testString + ''' doesn't have a proper "Alice eats apples" sentence''')

def main():
    testlist = ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.',
            'BOB EATS CATS.','Robocop eats apples.','ALICE THROWS FOOTBALLS.','Carol eats 7 cats.',
            'Alice chucks baseballs','Bob pets cats']
    for n in testlist:
        aliceEatsApples(n)

if __name__ == "__main__":
    main()
