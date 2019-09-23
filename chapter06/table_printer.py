tableData = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs','cats','moose','goose']]

max_len = []

def printTable(listlist):
    for columns in range(len(listlist)):
        print(listlist[columns])
        for items in range(len(listlist[columns])):
            if max_len[columns] < len(listlist[columns][items]):
                max_len[columns] = len(listlist[columns][items])
                

def main():
    printTable(tableData)

if __name__ == "__main__":
    main()
