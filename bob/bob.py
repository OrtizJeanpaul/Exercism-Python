def response(hey_bob):
    if hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!"

    if hey_bob.strip()[-1] == '?':#hey_bob.endswith("?")
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"

    return "Whatever."



