day_input = [i.strip() for i in open("day.input")]
test_input = [i.strip() for i in open("test.input")]

hands = {
    "A": "R",
    "X": "R",
    "B": "P",
    "Y": "P",
    "C": "S",
    "Z": "S"
}

points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


def calculate_winner(elf_play, human_play):
    if hands[elf_play] == hands[human_play]:
        return 3
    if hands[elf_play] == "R":
        if hands[human_play] == "P":
            return 6
        if hands[human_play] == "S":
            return 0
    if hands[elf_play] == "P":
        if hands[human_play] == "R":
            return 0
        if hands[human_play] == "S":
            return 6
    if hands[elf_play] == "S":
        if hands[human_play] == "R":
            return 6
        if hands[human_play] == "P":
            return 0



def count_points(input):
    hand_points = 0
    for game in input:
        hand = game.split(" ")
        win_points = calculate_winner(hand[0], hand[1])
        move_points = points[hand[1]]
        hand_points +=  win_points + move_points
    return hand_points





print(count_points(day_input))