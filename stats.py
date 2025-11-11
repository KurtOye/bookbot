def get_num_words(text):
    return len(text.split())

def get_letter_count(text):
    letters = {}
    for char in text:
        lower_char = char.lower()
        letters[lower_char] = letters.get(lower_char, 0) + 1
    return letters

def sort_letter_count(letter_dict):
    sorted_list = [{"char": c, "num": n} for c,n in letter_dict.items() if c.isalpha()]

    def sort_on(d):
        return d["num"]

    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list