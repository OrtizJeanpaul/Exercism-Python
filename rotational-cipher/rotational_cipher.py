from string import ascii_lowercase

def rotate(text, key):
    char_list = ascii_lowercase
    rotation_value = int(key.replace("ROT",""))
    mapped_chars = dict()
    

    for index in len(char_list):
        temp = char_list[index]
        mapped_chars[temp] = char_list[(rotation_value + index)%26]
    
    result = ""
    for char in enumerate(text):
        if char == " ":
            result += " "
        if mapped_chars.__contains__(char.lower()):
            cypher_value = mapped_chars.get(char.lower())
            if char.islower():
                result += cypher_value
            else:
                result += cypher_value.upper()
    
    return result