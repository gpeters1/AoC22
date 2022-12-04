day_input = [i.strip() for i in open("day.input")]
test_input = [i.strip() for i in open("test.input")]


def get_list(start_pair, end_pair):
    clean_list = []
    for i in range(int(start_pair), int(end_pair)+1):
        clean_list.append(i)
    return clean_list


def convert_to_list(pairs):
    unconverted_pair_1, unconverted_pair_2 = pairs.split(",")
    start_pair_1, end_pair_1 = unconverted_pair_1.split("-")
    clean_list_1 = get_list(start_pair_1, end_pair_1)
    start_pair_2, end_pair_2 = unconverted_pair_2.split("-")
    clean_list_2 = get_list(start_pair_2, end_pair_2)
    return clean_list_1, clean_list_2


def is_fully_contained(pair_1, pair_2):
    if set(pair_1).issubset(set(pair_2)) or set(pair_2).issubset(set(pair_1)):
        return 1
    return 0


def count_fully_contained(section_assignments):
    total_fully_contained = 0
    for pairs in section_assignments:
        pair_1, pair_2 = convert_to_list(pairs)
        total_fully_contained += is_fully_contained(pair_1, pair_2)
    return total_fully_contained


print(count_fully_contained(day_input))