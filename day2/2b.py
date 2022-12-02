day_input = [i.strip() for i in open("day.input")]
test_input = [i.strip() for i in open("test.input")]

plays = {
    "X": {
        "A": "C",
        "B": "A",
        "C": "B"
    },
    "Y": {
        "A": "A",
        "B": "B",
        "C": "C"
    },
    "Z": {
        "A": "B",
        "B": "C",
        "C": "A"
    }

}



result = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

hands = {
    "A": 1,
    "B": 2,
    "C": 3
}


def play_to_make(elf_play, result_needed):
    return plays[result_needed][elf_play]


def count_points(input):
    total_points = 0
    print(input)
    for game in input:
        hand = game.split(" ")
        print(hand)
        play = play_to_make(hand[0], hand[1])
        print(play)
        hand_points = hands[play]
        print(hand_points)
        win_points = result[hand[1]]
        print(win_points)

        total_points +=  win_points + hand_points
    return total_points




# print(count_points(test_input))
print(count_points(day_input))