def response(hey_bob):
    hey_bop_copy = hey_bob
    if hey_bop_copy.replace(" ", "") == "":
        return "Fine. Be that way!"

    if hey_bob[-1] == '?':
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"

    return "Whatever."



#     **"Sure."**
#   This is his response if you ask him a question, such as "How are you?"
#   The convention used for questions is that it ends with a question mark.
# - **"Whoa, chill out!"**
#   This is his answer if you YELL AT HIM.
#   The convention used for yelling is ALL CAPITAL LETTERS.
# - **"Calm down, I know what I'm doing!"**
#   This is what he says if you yell a question at him.
# - **"Fine. Be that way!"**
#   This is how he responds to silence.
#   The convention used for silence is nothing, or various combinations of whitespace characters.
# - **"Whatever."**
#   This is what he answers to anything else.