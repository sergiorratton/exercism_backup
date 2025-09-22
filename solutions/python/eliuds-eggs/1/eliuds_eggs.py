def egg_count(display_value):
    numero = display_value
    lista_resto = []
    while numero > 0:
        resto = numero % 2
        lista_resto.append(str(resto))
        numero //= 2
    lista_resto.reverse()
    numero_binario = ""
    for item in lista_resto:
        numero_binario += item
    numero_ovos = numero_binario.count("1")
    return numero_ovos
    