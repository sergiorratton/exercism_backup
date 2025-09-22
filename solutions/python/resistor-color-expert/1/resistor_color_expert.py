def resistor_label(colors):
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
    
    dict_cores_tolerancia = {"grey" : "0.05%",
                            "violet" : "0.1%",
                            "blue" : "0.25%",
                             "green" : "0.5%",
                             "brown" : "1%",
                             "red" : "2%",
                             "gold" : "5%",
                             "silver" : "10%"
                            }
    lista_de_para = []
    if len(colors) == 1:
        valor = dict_cores_valores.get(colors[0])
        return f"{valor} ohms"
    if len(colors) == 4:
        tamanho = 2
    else:
        tamanho = 3
    for item in range(0, tamanho):
        nome_cor = colors[item]
        valor_cor = dict_cores_valores.get(nome_cor)
        lista_de_para.append(valor_cor)
    numero_str = ""
    for digito in lista_de_para:
        numero_str += str(digito)
    numero_inteiro = int(numero_str)
    zeros = dict_cores_valores.get(colors[tamanho])
    potencia = 10 ** zeros
    numero_final = numero_inteiro * potencia
    item_tolerancia = colors[-1]
    tolerancia = dict_cores_tolerancia.get(item_tolerancia)
    if numero_final < 1000:
        return f"{numero_final} ohms ±{tolerancia}"
    elif numero_final < 1000000:
        numero_final /= 1000
        if numero_final % 1 == 0:
            numero_final = int(numero_final)
        return f"{numero_final} kiloohms ±{tolerancia}"
    else:
        numero_final /= 1000000
        if numero_final % 1 == 0:
            numero_final = int(numero_final)
        return f"{numero_final} megaohms ±{tolerancia}"