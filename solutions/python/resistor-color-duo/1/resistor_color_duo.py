def value(colors):
    dict_cores_valores = {"black" : 0,
                          "brown" : 1,
                          "red" : 2,
                          "orange" : 3,
                          "yellow" : 4,
                          "green" : 5,
                          "blue" : 6,
                          "violet" : 7,
                          "grey" : 8,
                          "white" : 9
                         }
    lista_de_para = []
    for item in range(0, 2):
        nome_cor = colors[item]
        valor_cor = dict_cores_valores.get(nome_cor)
        lista_de_para.append(valor_cor)
    numero_str = ""
    for digito in lista_de_para:
        numero_str += str(digito)
    numero_inteiro = int(numero_str)
    return numero_inteiro