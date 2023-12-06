with open("input.txt", "r") as f:
    total_calibrations = 0
    calibrations = {}
    for line_no, line in enumerate(f.readlines()):
        calibrations = {"s": -1, "e": -1}
        for c in line:
            if c.isdigit():
                if calibrations["s"] == -1:
                    calibrations["s"] = c
                calibrations["e"] = c
        total_calibrations += int(f"{calibrations['s'] + calibrations['e']}")

print(total_calibrations)