def color_code(color):
    codigos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cores = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    if color in cores:
        posicao_cor = cores.index(color)
        numero_cor = codigos[posicao_cor]
        return numero_cor
    else:
        return "Cor não encontrada."
def colors():
    cores = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return cores