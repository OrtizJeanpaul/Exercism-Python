def response(hey_bob):
    if(hey_bob == ""):
        return "Fine. Be that way!"

    is_question = hey_bob[-1] == '?'
    hey_bob_letters = hey_bob.replace(" ","").strip()
    is_upper = True

    for index in range(len(hey_bob_letters)):
        if not hey_bob_letters[index].isupper():
            is_upper = False
            break

    if(is_question):
        if(is_upper):
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if(is_upper):
        return "Whoa, chill out!"

    return "Whatever."