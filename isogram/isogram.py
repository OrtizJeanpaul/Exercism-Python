def is_isogram(string):
    just_letter_string = string.replace(" ", "").replace("-","").lower()
    word_set = set(just_letter_string)

    return len(word_set) == len(just_letter_string)