def encode(plain_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    numeros = "1234567890"
    plain_text = plain_text.lower()
    encoded_text = ""
    contador = 0
    for i, letra in enumerate(plain_text):
        if letra == " ":
            continue
        if letra not in plain and letra not in numeros:
            continue
        contador += 1
        if letra in plain:
            posicao = plain.index(letra)
            letra_nova = cipher[posicao]
            encoded_text += letra_nova
        elif letra in numeros:
            encoded_text += letra
        else:
            pass
        if contador % 5 == 0:
            qtd_max = len(plain_text) - 2
            if i == qtd_max:
                continue
            else:
                encoded_text += " "
    return encoded_text

def decode(ciphered_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    ciphered_text = ciphered_text.lower()
    decoded_text = ""
    for letra in ciphered_text:
        if letra in cipher:
            posicao = cipher.index(letra)
            letra_nova = plain[posicao]
            decoded_text += letra_nova
        elif letra == " ":
            pass
        else:
            decoded_text += letra
    return decoded_text