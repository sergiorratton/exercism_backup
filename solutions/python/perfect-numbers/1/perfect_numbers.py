def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        lista_numeros_divisores = []
        for i in range(1, number):
            if number % i == 0:
                lista_numeros_divisores.append(i)
        soma_lista = sum(lista_numeros_divisores)
        if number == soma_lista:
            return "perfect"
        elif number < soma_lista:
            return "abundant"
        else:
            return "deficient"
        
