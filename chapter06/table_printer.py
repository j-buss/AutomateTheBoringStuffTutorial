tableData = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs','cats','moose','goose']]

def printTable(listoflists):
    numberoflists = len(listoflists)
    numberofitems = len(listoflists[0]) # assuming that all inner lists are the same size
    maxoflists = []
    for innerlist in listoflists:
        maxlen = len(max(innerlist, key=len))
        maxoflists.append(maxlen)
    for i in range(numberofitems): # of items
        for j in range(numberoflists): # of lists
            print(listoflists[j][i].rjust(maxoflists[j]),' ',end='',sep='')
        print()

def main():
    printTable(tableData)

if __name__ == "__main__":
    main()
