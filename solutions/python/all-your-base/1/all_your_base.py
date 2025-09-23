def rebase(input_base, digits, output_base):
    tamanho = len(digits)
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if digits == [] or digits == [0]:
        lista_final = [0]
        return lista_final
    i = 0
    while i < tamanho:
        if digits[i] != 0:
            break
        i += 1
        if i == len(digits):
            lista_final = [0]
            return lista_final
    numero = 0
    iteracao = 0
    for valor in digits:
        numero_atual = valor * (input_base ** ((tamanho - 1) - iteracao))
        numero += numero_atual
        iteracao += 1
    resultado = ""
    while numero > 0:
        resto = numero % output_base
        if resto < 10:
            resultado = str(resto) + resultado
        else:
            resultado = chr(ord('A') + resto - 10) + resultado
        numero = numero // output_base
    lista_resultado = []
    if output_base <= 10:
        for char in resultado:
            char_int = int(char)
            lista_resultado.append(char_int)
        return lista_resultado
    else:
        for char in resultado:
            if char == "A":
                char = 10
            if char == "d":
                char = 45
            char = int(char)
            lista_resultado.append(char)
        return lista_resultado