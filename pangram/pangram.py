def is_pangram(sentence):
    sentence.replace(' ','')
    letter_set = set()
    for letter in sentence:
        if letter.lower().isalpha():
            letter_set.add(letter)
    return len(letter_set) == 26
    
    
        
        
