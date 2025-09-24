def count_words(sentence):
    sentence = sentence.lower()
    for letra in sentence:
        if letra.isalnum() == False:
            if letra != "'":
                sentence = sentence.replace(letra, " ")
    lista_palavras = sentence.split()
    contador = 0
    for item in lista_palavras:
        if item.isalnum() == False:
            for letra in item:
                if letra.isalnum() == False:
                    if letra == "'":
                        if item.index(letra) == 0 or item.index(letra) == (len(item) - 1):
                            string_subst = lista_palavras[contador]
                            string_subst = string_subst.strip("'")
                            lista_palavras[contador] = string_subst
                    elif letra != "'":
                            string_subst = lista_palavras[contador]
                            string_subst = string_subst.replace(letra, "")
                            lista_palavras[contador] = string_subst
                else:
                    continue
        contador += 1
    for item in lista_palavras:
        if item == "":
            lista_palavras.remove(item)
    dict_palavras = {}
    for item in lista_palavras:
        dict_palavras[item] = 1
    for item in lista_palavras:
        contagem = lista_palavras.count(item)
        dict_palavras.update({item : contagem})
    return dict_palavras