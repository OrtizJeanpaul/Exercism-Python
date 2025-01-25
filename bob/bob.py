def response(hey_bob):
    if(hey_bob == ""):
        return "Fine. Be that way!"
    if(hey_bob[-1] == '?'):
        temp = hey_bob.replace(" ","")
        if(temp[0].isUpper() and temp[1].isUpper()):
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if(hey_bob[0].isUpper() and hey_bob[1].isUpper()):
        return "Whoa, chill out!"
    return "Whatever"