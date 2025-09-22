def translate(text):
    texto_separado = text.lower().split()
    vogais = ("a", "e", "i", "o", "u")
    lista_traduzida = []
    for palavra in texto_separado:
        palavra_traduzida = ""
        # Regra 1
        if palavra.startswith(vogais) or palavra.startswith("xr") or palavra.startswith("yt"):
            palavra_traduzida = palavra + "ay"

        # Regra 3
        elif "qu" in palavra:
            indice_qu = palavra.find("qu")
            if indice_qu == 0:
                palavra_traduzida = palavra[2:] + palavra[:2] + "ay"
            elif indice_qu > 0:
                all_pre_qu_are_consonants = True
                for char_before_qu in palavra[:indice_qu]:
                    if char_before_qu in vogais:
                        all_pre_qu_are_consonants = False
                        break
                if all_pre_qu_are_consonants:
                    palavra_traduzida = palavra[indice_qu + 2:] + palavra[:indice_qu + 2] + "ay"

        # Regra 4
        elif "y" in palavra and not palavra.startswith(vogais):
            vogal_ou_y = -1
            for i, char in enumerate(palavra):
                if char in vogais:
                    vogal_ou_y = i
                    break
                if char == 'y' and i > 0:
                    vogal_ou_y = i
                    break
            if vogal_ou_y > 0:
                consonant_cluster = palavra[:vogal_ou_y]
                palavra_traduzida = palavra[vogal_ou_y:] + consonant_cluster + "ay"
            elif vogal_ou_y == 0 and palavra.startswith("y"):
                 consonant_cluster = palavra[0]
                 palavra_traduzida = palavra[1:] + consonant_cluster + "ay"
            else:
                pass
            
        # Regra 2
        if not palavra_traduzida:
            consonant_cluster = ""
            for i, char in enumerate(palavra):
                if char not in vogais and not (char == 'y' and i > 0):
                    consonant_cluster += char
                else:
                    break
            if consonant_cluster:
                palavra_traduzida = palavra[len(consonant_cluster):] + consonant_cluster + "ay"
            else:
                palavra_traduzida = palavra + "ay"

        lista_traduzida.append(palavra_traduzida)

    final_text = " ".join(lista_traduzida)
    return final_text