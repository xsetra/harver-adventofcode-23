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

def parse_gameset(game_set):
    vals = {"red": 0, "green": 0, "blue": 0}
    for s in game_set.split(","):
        result = s.split(" ")
        amount = int(result[1])
        color = result[2].strip("\n")
        vals[color] = amount
    return vals            
        


with open("input2.txt", "r") as f:
    total = 0
    for l in f.readlines():
        line = l.split(":")
        game_no = line[0].split(" ")[-1]
        game_sets = line[1].split(";")

        values = [0, 0, 0]
        for g_set in game_sets:
            vals = parse_gameset(g_set)
            values[0] = vals['red'] if vals['red'] > values[0] else values[0]
            values[1] = vals['green'] if vals['green'] > values[1] else values[1]
            values[2] = vals['blue'] if vals['blue'] > values[2] else values[2]
        
        multiplies = values[0] * values[1] * values[2]
        total += multiplies
    
    print(total)
    
            