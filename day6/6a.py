day_input = [i.strip() for i in open("day.input")][0]
test_input = [i.strip() for i in open("test.input")][0]

print(test_input)




def first_marker_character(data):
    marker_searcher = []
    for i in range(0, len(data)):
        print(marker_searcher)
        marker_searcher.append(data[i])
        print(marker_searcher)
        if len(set(marker_searcher)) == 4:
            return i+1
        if len(marker_searcher) < 4:
            continue
        marker_searcher.pop(0)
        print(marker_searcher)
        

print(first_marker_character(day_input))