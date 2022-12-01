day_input = [i.strip() for i in open("test.input")]
print(day_input)
def most_calories(food):
    maximum_food = 0
    no_of_calories = 0
    for i in food:
        if i == '':
            if no_of_calories > maximum_food:
                maximum_food = no_of_calories
            no_of_calories = 0
            continue
        no_of_calories += int(((i)))
    return maximum_food


maximum_food = most_calories(day_input)
print(maximum_food)