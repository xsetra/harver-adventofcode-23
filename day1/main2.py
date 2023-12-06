mapping_letter = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

with open("input2.txt", "r") as f:
    total_calibrations = 0
    calibrations = {}
    for line_no, line in enumerate(f.readlines()):
        
        digit_indexes = {}
        for no, letter in enumerate(mapping_letter):
            if no == "zero":
                continue
            try:
                s = 0
                while (len(line) - len(letter) - s) > 0:
                    _ = line.index(letter, s)
                    digit_indexes[_] = no
                    s = _ + len(letter)                
            except: 
                pass

        for c_no, c in enumerate(line):                
            if c.isdigit():
                digit_indexes[c_no] = int(c)

        all_indexes = list(digit_indexes.keys())
        all_indexes.sort()
        # number = f"{digit_indexes[all_indexes[0]]}{digit_indexes[all_indexes[-1]]}"
        # print(f"{number} = {line}")
        number = f"{digit_indexes[all_indexes[0]]}{digit_indexes[all_indexes[-1]]}"
        total_calibrations += int(number)

print(total_calibrations)