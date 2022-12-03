day_input = [i.strip() for i in open("day.input")]
test_input = [i.strip() for i in open("test.input")]


def get_same_items(group_rucksacks):
    bag1, bag2, bag3 = tuple(group_rucksacks)
    for item_1 in bag1:
        for item_2 in bag2:
            for item_3 in bag3:
                if item_1 == item_2 == item_3:
                    return item_1

def calculate_priority(rucksacks):
    total_score = 0
    group_rucksacks = []
    for rucksack in rucksacks:
        group_rucksacks.append(rucksack)
        if len(group_rucksacks) == 3:
            same_item = get_same_items(group_rucksacks)
            total_score += find_position(same_item)
            group_rucksacks = []
            continue

    return total_score

def find_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(letter) + 1
    return (alphabet)


print(calculate_priority(day_input))
# find_position("p")