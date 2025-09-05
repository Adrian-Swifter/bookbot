def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_characters(text):
    fine_grained_text = text.lower()
    chars_dict = {}
    for char in fine_grained_text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_dictionary(d):
    new_list = []
    for key, value in d.items():
        if key.isalpha():
            new_list.append({"char": key, "num": value})
    new_list.sort(key=sort_on, reverse=True)
    return new_list

def sort_on(items):
    return items["num"]