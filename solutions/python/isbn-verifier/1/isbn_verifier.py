def is_valid(isbn):
    lista_multiplicadores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    isbn = isbn.upper()
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    lista_strings = list(isbn)
    if not lista_strings[-1].isnumeric():
        if lista_strings[-1] == "X":
            lista_strings[-1] = "10"
        else:
            return False
    lista_numeros = []
    for numero_string in lista_strings:
        if not numero_string.isnumeric():
            return False
        else:
            numero_convertido = int(numero_string)
            lista_numeros.append(numero_convertido)
    resultado_multiplicacao = []
    for posicao in range(len(lista_numeros)):
        resultado_multiplicacao.append(lista_numeros[posicao] * lista_multiplicadores[posicao])
    resultado_final = sum(resultado_multiplicacao) % 11
    if resultado_final == 0:
        return True
    else:
        return False