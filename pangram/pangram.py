def is_pangram(sentence):
    sentence.lower().replace(' ','')
    letter_set = set()
    for index in sentence:
        if sentence[index].isAlpha():
            letter_set += sentence[index]
    return len(letter_set) == 26
    
    
        
        
