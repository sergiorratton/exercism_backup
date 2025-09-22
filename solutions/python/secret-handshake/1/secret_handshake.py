def commands(binary_str):
    comandos_finais = []
    dict_pos = {
                4 : "wink",
                3 : "double blink",
                2 : "close your eyes",
                1 : "jump"
                }
    binary_str = binary_str.zfill(5)
    contador = 0
    for digito in binary_str:
        posicao_digito = contador
        if posicao_digito == 0:
            contador += 1
            continue
        if digito == "1":
            comando = dict_pos[posicao_digito]
            comandos_finais.append(comando)
            contador += 1
        else:
            contador += 1
            continue
    comandos_finais.reverse()
    if binary_str[0] == "1":
        comandos_finais.reverse()
    return comandos_finais

commands("00011")