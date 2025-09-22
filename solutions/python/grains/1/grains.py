def square(number):
    if number not in range(1, 65) or not isinstance(number, int):
        raise ValueError("square must be between 1 and 64")
    else:
        wheat_grains = 2 ** (number - 1)
        return wheat_grains


def total():
    valor_total = 0
    for number in range(1, 65):
        valor_total = valor_total + (2 ** (number - 1))
    return valor_total