def is_pangram(sentence):
    sentence.lower().replace(' ','')
    letter_set = set(sentence)

    return len(letter_set) == 26
    
    
        
        
