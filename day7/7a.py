day_input = [i.strip() for i in open(r"c:\Users\gpeters\OneDrive - CACI Ltd\Documents\AoC\AoC22\day7\day.input")]
easy_test_input = [i.strip() for i in open(r"c:\Users\gpeters\OneDrive - CACI Ltd\Documents\AoC\AoC22\day7\easy_test.input")]
test_input = [i.strip() for i in open(r"c:\Users\gpeters\OneDrive - CACI Ltd\Documents\AoC\AoC22\day7\test.input")]


FOLDERS = {}
# print(test_input)

def add_to_folder(command, folder):
    if command.startswith("$ ls"):
        return folder
    if command.startswith("dir"):
        return folder
    file_size, file_name = command.split()
    folder.update({file_name: file_size})
    return folder



def create_directory(data, folder):
    if not data:
        return data, folder
    command = data.pop(0)
    if command.startswith("$ cd"):
        change_directory = command.split()[-1]
        if change_directory == "..":
            return data, folder
        data, sub_folder = create_directory(data, {})
        folder[change_directory] = sub_folder

        # return (data, folder)
    else:
        folder = add_to_folder(command, folder)
        # folder = {**folder, **new_folder}
    return create_directory(data, folder)

    # return (data, folder)
        



def add_to_folder_1(command):
    if command.startswith("$ cd"):
        return 0
    if command.startswith("$ ls"):
        return 0
    file_size, file_name = command.split()
    return int(file_size)



def create_directory_1(data, folder_points):
    if not data:
        return data, folder_points
    command = data.pop(0)
    # print(command)
    # print(folder_points)
    if command.startswith("$ cd"):
        change_directory = command.split()[-1]
        if change_directory == "..":
            return data, folder_points
        data, sub_folder_points = create_directory_1(data, 0)
        FOLDERS.update({change_directory: sub_folder_points})
        folder_points += sub_folder_points
        # folder[change_directory] = sub_folder

        # data, folder_points = create_directory_1(data, folder_points)
    if command.startswith("dir"):
        sub_directory = command.split()[-1]
        # data, folder_points = create_directory_1(data, folder_points)

        # folder.update({sub_directory: {}})
        # data, folder_points = create_directory(data, folder_points)
    else:
        folder_points += add_to_folder_1(command)
        # data, folder_points = create_directory(data, folder_points)
        # folder = {**folder, **new_folder}
        # data, folder_points = create_directory(data, folder_points)
    # data, folder_points = create_directory(data, folder_points)
    return create_directory_1(data, folder_points)
        
    # return (data, folder_points)
        


def count_objects(folder, score):
    # print(folder)
    score = 0
    for key,value in folder.items():
        if type(value) is dict:
            new_score = count_objects(value, 0)
            FOLDERS.update({key: new_score})
            score += new_score
            continue
        else:
            score += int(value)
    return score

def total_size(data):
    (data.pop(0))
    data, folder = create_directory_1(data, 0)

    # result = {"/": folder}
    # print(result)
    # count_objects(result, 0)
    # print(FOLDERS)

    # FOLDERS.update(result)
    # print(result)
    sum = 0
    # print(FOLDERS)
    for key, value in FOLDERS.items():
        if value <= 100000:
            print(key)
            sum += value

    print(sum)
# total_size(easy_test_input)
total_size(day_input)
# total_size(test_input)
# print(FOLDERS)
# total_size(day_input)