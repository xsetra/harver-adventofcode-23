LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_valid(game_set):
    for s in game_set.split(","):
        result = s.split(" ")
        amount = int(result[1])
        color = result[2].strip("\n")
        if amount > LIMITS[color]:
            return False
    return True
            
        


with open("input.txt", "r") as f:
    total = 0
    for l in f.readlines():
        line = l.split(":")
        game_no = line[0].split(" ")[-1]
        game_sets = line[1].split(";")

        total += int(game_no)
        for g_set in game_sets:
            if not is_valid(g_set):
                total -= int(game_no)
                break
    
    print(total)
            