def find_anagrams(word, candidates):
    anagramas = []
    org_palavra = sorted(word.lower())
    for palavra in candidates:
        if palavra.lower() == word.lower():
            continue
        palavra_candidata = sorted(palavra.lower())
        if org_palavra == palavra_candidata:
            anagramas.append(palavra)
    return anagramas