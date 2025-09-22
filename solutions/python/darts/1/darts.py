def score(x, y):
    raio_interno = 1
    raio_medio = 5
    raio_externo = 10
    distancia = (((x-0) ** 2) + ((y-0) ** 2)) ** 0.5
    if distancia > raio_interno:
        if distancia > raio_medio:
            if distancia > raio_externo:
                pontos = 0
            else:
                pontos = 1
        else:
            pontos = 5
    else:
        pontos = 10
    return pontos