import numpy as np
import random


def generate_random_sudoku():
    ''' Unmodified code from sudoku_generator.final.py '''
    base = 3  # Base size of the Sudoku puzzle (3x3 blocks)
    side = base * base

    # Pattern for a baseline valid solution
    def pattern(r, c): return (base*(r % base) + r//base + c) % side

    # Randomize rows, columns, and numbers (of valid base pattern)
    def shuffle(s): return random.sample(s, len(s))

    r_base = range(base)
    rows = [g*base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g*base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, side + 1))

    # Produce a board using the randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    # Remove random cells to create the puzzle
    squares = side * side
    empties = random.randint(35, 60)  # Number of empty cells (adjust for difficulty)
    for _ in range(empties):
        row = random.randint(0, side - 1)
        col = random.randint(0, side - 1)
        board[row][col] = 0

    return np.array(board)



def deconstruct_sudoku(sudoku):
    ''' Deconstructs given sudoku into rows, columns, and boxes '''
    rows = sudoku
    columns = sudoku.transpose()
    boxes = [ [], [], [], [], [], [], [], [], []]
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            box = determine_box(i, j)
            boxes[box].append(sudoku[i][j])
    boxes = np.array(boxes)
    return rows, columns, boxes


def get_possible_values(row, column, box):
    ''' Get all possible values for a given cell '''
    p = []
    for i in range(len(sudoku)):
        if i not in row and i not in box and i not in column:
            p.append(i)
    return p


def solve_sudoku(sudoku):
    ''' Algorithm to solve sudoku using hill climbing '''
    s = sudoku.copy()
    # gets arrays of all rows columns and boxes for convenience
    r, c, b = deconstruct_sudoku(s)
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            # Loop iterates through every cell once
            if sudoku[i][j] == 0:
                row = r[i]
                column = c[j]
                box = b[determine_box(i, j)]
                possible_vals = get_possible_values(row, column, box)
                if len(possible_vals) > 0:
                    random_val = possible_vals[random.randint(0, len(possible_vals)-1)]
                else: # No possible values that won't cause error
                    random_val = random.randint(1, 9)
                # update all values
                s[i][j] = random_val
                row[j] = random_val
                column[i] = random_val
                box_element = ((i%3)*3) + (j%3)
                box[box_element] = random_val
    return s


def calculate_error(sudoku):
    ''' Calculates the amount of errors in a sudoku.
     
        Uses the rules that there must be only one set of repeating digits in very row column and box.
        EVery time one rule is broken, the error increases by one.
    '''
    r, c, b = deconstruct_sudoku(sudoku)
    total_error = 0
    for i in range(len(sudoku)):
        row_error = len(sudoku) - len(np.unique(r[i]))
        column_error = len(sudoku) - len(np.unique(c[i]))
        box_error = len(sudoku) - len(np.unique(b[i]))
        total_error += row_error + column_error + box_error
    return total_error


def determine_box(r, c):
    ''' Determines the box a cell resides in '''
    a = int(r/3) * 3
    b = int(c/3)
    return a+b


if __name__ == '__main__':
    iterations = 10000
    sudoku = generate_random_sudoku()
    print("Starting Sudoku:")
    print(sudoku)
    print()
    current_solution = solve_sudoku(sudoku)
    current_error = calculate_error(current_solution)
    print("First Solution:")
    print(current_solution)
    print("Error:", current_error)
    print()
    for i in range(iterations):
        solution = solve_sudoku(sudoku)
        error = calculate_error(solution)
        if error < current_error:
            print(f"Updated solution from {current_error} errors to {error} errors!")
            current_solution = solution
            current_error = error
        if error == 0:
            break
    print()
    print("Iterations:", iterations)
    print("Final Solution:")
    print(current_solution)
    print("Error:", current_error)
    print()
    print("-------------------------------------------------------------------------------")
    print()
