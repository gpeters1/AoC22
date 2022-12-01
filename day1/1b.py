day_input = [i.strip() for i in open("day.input")]
print(day_input)
def most_calories(food):
    maximum_food = [0,0,0]
    print(maximum_food)
    no_of_calories = 0
    for i in food:
        # print(i)
        if i == '':
            maximum_food.append(no_of_calories)
            maximum_food.sort(reverse=True)
            print(maximum_food)
            maximum_food.pop(3)
            print(maximum_food)
            no_of_calories = 0
            continue
        no_of_calories += int(((i)))
        print(no_of_calories)
    maximum_food.append(no_of_calories)
    maximum_food.sort(reverse=True)
    print(maximum_food)
    maximum_food.pop(3)        
    total_calories = 0
    for i in maximum_food:
        total_calories += i
    return total_calories



maximum_food = most_calories(day_input)
print(maximum_food)