def rotate(text, key):
    # Pedindo ao usuário para colocar a frase, seja ela codificada ou não
    msg_input = text
    pulo = key
    comp_msg = len(msg_input)
    msg_output = list()
    
    # Caso o pulo seja maior que a quantidade de letras do alfabeto, diminuir para que volte ao máximo de 26
    while pulo >= 26:
        pulo = pulo - 26
        if pulo < 26:
            break
    
    # Iterando cada caractere da string input
    for i in range(0, comp_msg):
        # Testando se o caractere i é letra ou não
        if msg_input[i].isalpha():
            # Testando se o caractere é maiúsculo
            if msg_input[i].isupper():
                # Transformando o caractere em ascii para poder fazer operações matemáticas, como o pulo
                asc_temp = ord(msg_input[i])
                # Testando se o pulo levará a um código ascii além do alfabeto maiúsculo
                if asc_temp + pulo > 90:
                    asc_temp_novo = chr(asc_temp - 26 + pulo)
                else:
                    asc_temp_novo = chr(asc_temp + pulo)
                msg_output.append(asc_temp_novo)
            # Caso seja minúsculo:
            else:
            # Transformando o caractere em ascii para poder fazer operações matemáticas, como o pulo
                asc_temp = ord(msg_input[i])
                # Testando se o pulo levará a um código ascii além do alfabeto minúsculo
                if asc_temp + pulo > 122:
                    asc_temp_novo = chr(asc_temp - 26 + pulo)
                else:
                    asc_temp_novo = chr(asc_temp + pulo)
                msg_output.append (asc_temp_novo)
        # Caso não seja letra:
        else:
            msg_output.append(msg_input[i])
    msg_final = ''.join(str(item) for item in msg_output)
    return msg_final