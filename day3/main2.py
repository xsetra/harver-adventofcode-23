matrix = []
with open("input2.txt", "r") as f:
    for line in f.readlines():
        row = []
        line = line.strip("\n")
        for c in line: 
            row.append(c)
        matrix.append(row)

def isstar(cell_value: str) -> bool:
    if cell_value == "*":
        return True
    return False


def check_is_adjacent_to_star(row_no, col_no) -> tuple | None:
    try:
        # clockwise check
        for i in range(-1, 2): # produces -1, 0, 1
            for j in range(-1, 2): 
                if isstar(matrix[row_no + i][col_no + j]):
                    return (row_no + i, col_no +j)
        return None
    except IndexError: 
        ...




def insert_number(all_stars, star_position, new_number):
    records = all_stars.get(f"{star_position[0]},{star_position[1]}", [])
    records.append(int(number))
    all_stars[f"{star_position[0]},{star_position[1]}"] = records
    return all_stars



total = 0
stars = {}

for row_no, rows in enumerate(matrix):
    number = ""
    is_included = False
    star_position = None

    for col_no, col in enumerate(rows):
        if col.isdigit():
            number += col
            if not is_included:
                s = check_is_adjacent_to_star(row_no, col_no)
                if s is not None:
                    star_position = (s[0], s[1])
                    is_included = True
            
            try:
                # Next item isn't digit, sum into total if it has adjacent symbol
                if not rows[col_no + 1].isdigit():
                    if is_included:
                        stars = insert_number(stars, star_position, number)
                        
            except IndexError:
                if is_included:
                    stars = insert_number(stars, star_position, number)
        else:
            # Reset, column isn't a digit.
            number = ""
            is_included = False
            star_position = None


for star in stars.keys():
    part_numbers = stars[star]
    if len(part_numbers) == 2:
        total += (part_numbers[0] * part_numbers[1])

print(total)




