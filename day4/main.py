import parse, math

winner_format = " {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} "
number_format = " {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d}"


total = 0

def card_parser(card):
    cols = card.split(":")
    numbers = cols[1].split("|")
    
    winner_numbers = parse.parse(winner_format, numbers[0])
    numbers_we_have = parse.parse(number_format, numbers[1].strip("\n"))
    # print(numbers)
    # print("---")
    # print(winner_numbers)
    # print(numbers_we_have)

    return (winner_numbers, numbers_we_have)


with open("input.txt", "r") as f:
    for card in f.readlines():
        wins, nums = card_parser(card)
        wins = tuple(wins)
        nums = tuple(nums)
        point = 0
        for n in nums:
            if n in wins:
                point += 1
        
        if point != 0:
            pow = (point - 1)
            total += (2 ** pow)
    print(total)
