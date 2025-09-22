def steps(number):
    contador = 0
    if isinstance(number, int) and number > 0:
        while number != 1:
            if number % 2 == 0:
                number /= 2
            else:
                number = (number * 3) + 1
            contador += 1
    else:
        raise ValueError("Only positive integers are allowed")
    return contador