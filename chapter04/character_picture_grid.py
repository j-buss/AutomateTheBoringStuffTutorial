grid = [['.','.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def print_grid(grid_input):
    num_rows = len(grid_input)
    elements_in_row = len(grid_input[0]) 
    
    for element in range(elements_in_row): 
        for row in range(num_rows):
            print(grid_input[row][element], end = '')
        print()


def main():
    print_grid(grid)

if __name__ == "__main__":
    main()
