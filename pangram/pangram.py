def is_pangram(sentence):
    sentence.toLower().replace(' ','')
    letter_set = set(sentence)

    return len(letter_set) == 26
    
    
        
        
