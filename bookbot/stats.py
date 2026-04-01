def count_words(file_string):
    file_arr = file_string.split()
    return len(file_arr)

def count_char(file_string):
    char_dict = {}
    file_string = file_string.lower()
    for char in file_string:
        if char not in char_dict.keys():
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items["num"]


def sort_char_dict(char_dict):
    char_list = []
    for key,value in char_dict.items():
        char_list.append({"char": key, "num": value})

    char_list.sort(reverse=True, key=sort_on)

    return(char_list)