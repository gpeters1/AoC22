day_input = [list(j) for j in [i.strip() for i in open(r"c:\Users\gpeters\OneDrive - CACI Ltd\Documents\AoC\AoC22\day8\day.input")]]
test_input = [list(j) for j in [i.strip() for i in open(r"c:\Users\gpeters\OneDrive - CACI Ltd\Documents\AoC\AoC22\day8\test.input")]]

print(test_input)




def count_visible(data):
    visible_trees = 0
    for row in range(0, len(data)):
        for column in range(0, len(data[row])):
            print(data[row][column], end='')
            director_up = -1
            director_down = 1
            director_left = -1
            director_right = 1
            break_loop = False
            if row == 0:
                visible_trees += 1
                continue
            while row+director_up >= 0:

                if data[row+director_up][column] < data[row][column]:
                    print(data[row+director_up][column])
                    print(data[row][column])
                if row+director_up < 0:
                    visible_trees += 1
                    break_loop = True
                director_up -= 1
            if break_loop:
                continue
            # if row+director_down > len(data[row]):
            #     visible_trees += 1
            #     continue
            # while data[row+director_down][column] < data[row][column]:
            #     director_down += 1
            # if row+director_left < 0:
            #     visible_trees += 1
            #     continue
            # while data[row+director_left][column] < data[row+director_up][column]:
            #     director_up += 1

        print()
    print(visible_trees)


count_visible(test_input)