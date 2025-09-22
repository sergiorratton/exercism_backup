def convert(number):
    divisao3 = number % 3
    divisao5 = number % 5
    divisao7 = number % 7
    str_retorno = ""
    if divisao3 == 0:
        str_retorno = str_retorno + "Pling"
        
    if divisao5 == 0:
            str_retorno = str_retorno + "Plang"
        
    if divisao7 == 0:
            str_retorno = str_retorno + "Plong"
        
    if divisao3 !=0 and divisao5 != 0 and divisao7 != 0:
        str_retorno = str(number)

    return str_retorno