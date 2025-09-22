def response(hey_bob):
    if hey_bob.isspace()or hey_bob == "":
        return "Fine. Be that way!"
    else:
        hey_bob = hey_bob.strip()
    if hey_bob[len(hey_bob) -1] == "?":
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."