def is_pangram(sentence):
    sentence.lower().replace(' ','')
    letter_set = set()
    for _,letter in sentence:
        if letter.isAlpha():
            letter_set += letter
    return len(letter_set) == 26
    
    
        
        
