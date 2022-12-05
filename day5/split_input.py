import re
test_input = [i.replace("\n", "") for i in open("day.input")]
print(test_input)
for line in test_input:
    board = (re.findall("\s{4}|[a-zA-Z]", line))
    moves = re.findall("[0-9]+", line)
    print(moves)
    

def split_input(input):
    input_1 = []
    input_2 = []
    split = 1
    for i in test_input:
        if not i:
            split += 1
            continue
        if i.startswith(" 1"):
            split += 1
        if split == 1:
            input_1.append(i)
        if split == 3: 
            input_2.append(i)
    return input_1, input_2

