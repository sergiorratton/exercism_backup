def is_pangram(sentence):
    letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    sentence = sentence.lower()
    for letter in letters:
        if letter not in sentence:
            return False
            break
    return True
    
