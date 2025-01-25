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
    if(is_upper and hey_bob[-1] == "!"):
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