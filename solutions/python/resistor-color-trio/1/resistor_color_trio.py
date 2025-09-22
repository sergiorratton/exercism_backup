def label(colors):
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    color_names = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    lista_de_para = []
    while len(colors) > 3:
        colors.pop() 
    for name in colors:
        posicao_nome_lista_original = color_names.index(name)
        # print(f"O índice do nome inserido {name} na lista original é: {posicao_nome_lista_original}")
        valor_posicao = values[posicao_nome_lista_original]
        # print(f"O valor relativo ao índice {posicao_nome_lista_original} na lista original é: {valor_posicao}")
        posicao_nome_lista_inserida = colors.index(name)
        # print(f"A posição do nome {name} na lista inserida é: {posicao_nome_lista_inserida}")
        if posicao_nome_lista_inserida < 2:
            lista_de_para.append(valor_posicao)
            # print(lista_de_para)
        else:
            for zeros in range(0, valor_posicao):
                zeros += 1
                lista_de_para.append(0)
            # print(lista_de_para)
        colors[colors.index(name)] = "-"
    numero_str = ""
    for digito in lista_de_para:
        numero_str += str(digito)
    numero_inteiro = int(numero_str)
    # print(f"O valor absoluto do número é: {numero_inteiro}")
    if numero_inteiro > 1000:
        numero_inteiro_dividido = numero_inteiro / 1000
        if numero_inteiro_dividido > 1000:
            numero_inteiro_dividido /= 1000
            if numero_inteiro_dividido > 1000:
                numero_inteiro_dividido /= 1000
                numero_inteiro_dividido = int(numero_inteiro_dividido)
                return f"{numero_inteiro_dividido} gigaohms"               
            else:
                numero_inteiro_dividido = int(numero_inteiro_dividido)
                return f"{numero_inteiro_dividido} megaohms"
        else:
            numero_inteiro_dividido = int(numero_inteiro_dividido)
            return f"{numero_inteiro_dividido} kiloohms"
    else:
        return f"{numero_inteiro} ohms"