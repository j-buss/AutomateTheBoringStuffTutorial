import collatz

def collatz_sequence():
    print('Enter number (integer):')
    result = int(input())
    while result != 1:
        result = collatz.collatz(result)
        print(result)
