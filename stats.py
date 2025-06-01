def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    counter = {}
    for character in text:
        character = character.lower()
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter

def sort_on_num(item):
    return item["num"]

def sort_char_count(counter_dict):
    result = []
    for char, count in counter_dict.items():
        entry = {"char": char, "num": count}
        result.append(entry)
    result.sort(reverse=True, key=sort_on_num)
    return result