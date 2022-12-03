day_input = [i.strip() for i in open("day.input")]
test_input = [i.strip() for i in open("test.input")]


def get_same_items(compartment_1, compartment_2):
    same_items = []
    for item_1 in compartment_1:
        for item_2 in compartment_2:
            if item_1 == item_2 and item_1 not in same_items:
                same_items.append(item_1)
    return same_items

def calculate_priority(rucksacks):
    total_score = 0
    for rucksack in rucksacks:
        compartment_1 = rucksack[:len(rucksack)//2]
        compartment_2 = rucksack[len(rucksack)//2:]
        same_items = get_same_items(compartment_1, compartment_2)
        for item in same_items:
            total_score += find_position(item)
    return total_score

def find_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(letter) + 1
    return (alphabet)


print(calculate_priority(day_input))
# find_position("p")