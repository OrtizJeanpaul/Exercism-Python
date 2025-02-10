def find_anagrams(word, candidates):
    sorted_word = "".join(sorted(word.lower()))
    anagrams = []
    for index in range(len(candidates)):
        temp = "".join(sorted(candidates[index].lower()))
        if temp == sorted_word and not candidates[index] == word:
            anagrams.append(candidates[index])
    
    return anagrams

