def is_armstrong_number(number):
    number_str = str(number)
    numero_digitos = len(number_str)
    soma = 0
    for indice, digito in enumerate(number_str):
        potencia = int(digito) ** numero_digitos
        soma += potencia
    if soma == number:
        return True
    else:
        return False