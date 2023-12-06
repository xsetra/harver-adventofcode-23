matrix = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        row = []
        line = line.strip("\n")
        for c in line: 
            row.append(c)
        matrix.append(row)

def issymbol(cell_value: str) -> bool:
    if cell_value.isalpha() or cell_value.isdigit() or cell_value == ".":
        return False
    return True


def check_is_adjacent_to_symbol(row_no, col_no) -> bool:
    try:
        # clockwise check
        for i in range(-1, 2): # produces -1, 0, 1
            for j in range(-1, 2): 
                if issymbol(matrix[row_no + i][col_no + j]):
                    return True
        return False
    except IndexError: 
        ...


def calculate(total, is_included, number):
    if is_included:
        total += int(number)
    return total


total = 0

for row_no, rows in enumerate(matrix):
    number = ""
    is_included = False

    for col_no, col in enumerate(rows):
        if col.isdigit():
            number += col
            if not is_included:
                if check_is_adjacent_to_symbol(row_no, col_no):
                    is_included = True
            
            try:
                # Next item isn't digit, sum into total if it has adjacent symbol
                if not rows[col_no + 1].isdigit():
                    total = calculate(total, is_included, number)
            except IndexError:
                total = calculate(total, is_included, number)
        else:
            # Reset, column isn't a digit.
            number = ""
            is_included = False
print(total)


