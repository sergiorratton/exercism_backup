def is_isogram(string):
    string_letras = string.lower()
    string_letras = string_letras.replace(" ", "")
    string_letras = string_letras.replace("-", "")
    for letter in range(0, len(string_letras)):
        if string_letras[letter] in string_letras[letter+1:]:
            return False
        else:
            pass
    return True