from string import ascii_lowercase

def rotate(text, key):
    char_list = ascii_lowercase
    mapped_chars = dict()
    

    for index in range(len(char_list)):
        temp = char_list[index]
        mapped_chars[temp] = char_list[(key + index)%26]
    
    result = ""
    for _,char in enumerate(text):
        if mapped_chars.__contains__(char.lower()):
            cypher_value = mapped_chars.get(char.lower())
            if char.islower():
                result += cypher_value
            else:
                result += cypher_value.upper()
        else:
            result += char
    return result