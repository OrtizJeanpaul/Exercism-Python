def is_pangram(sentence):
    sentence.lower().replace(' ','')
    for _,letter in sentence:
        if not letter.isAlpha():
            letter_set = set(sentence)

    return len(letter_set) == 26
    
    
        
        
