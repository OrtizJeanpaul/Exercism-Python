def find_anagrams(word, candidates):
    sorted_word = "".join(sorted(word.lower))
    anagrams = []
    for _, cand in enumerate(candidates):
        temp = "".join(sorted(cand.lower))
        if temp == sorted_word and not cand == word:
            anagrams.append(cand)
    
    return anagrams

