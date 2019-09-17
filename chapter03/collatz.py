def collatz(number):
    integer = int(number)
    if integer % 2 == 0:
        return integer // 2
    else:
        return 3 * integer + 1

def collatz_sequence():
    while True:
        print('Please enter a positive integer:')
        try:
            result = int(input())
            if result <= 0:
                continue
            while result != 1:
                result = collatz(result)
                print(result)
            break
        except ValueError:
            pass

def main():
    collatz_sequence()

if __name__ == "__main__":
    main()
