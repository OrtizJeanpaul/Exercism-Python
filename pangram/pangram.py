def is_pangram(sentence):
    sentence.lower().replace(' ','')
    letter_set = set()
    for letter in sentence:
        if letter.isalpha():
            letter_set.add(letter)
    return len(letter_set) == 26
    
    
        
        
