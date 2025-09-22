def annotate(garden):
    validos = [" ", "*"]
    lista_vazia = []
    lista_vazio = [""]
    if garden == lista_vazia or garden == lista_vazio:
        return garden
    for item in garden:
        for char in item:
            if char not in validos:
                raise ValueError("The board is invalid with current input.")
        index_item = garden.index(item)
        if index_item == 0 and len(garden) > 1:
            if len(item) != len(garden[index_item + 1]):
                raise ValueError("The board is invalid with current input.")
        elif index_item == len(garden) - 1 and len(garden) > 1:
            if len(item) != len(garden[index_item - 1]):
                raise ValueError("The board is invalid with current input.")
    garden = [list(row) for row in garden]
    linhas = len(garden)
    colunas = len(garden[0])
    for i, row in enumerate(garden):
        for j, char in enumerate(row):
            if char == "*":
                continue
            qtd_flores = 0
            vizinhos = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1),          (0, 1),
                        (1, -1),  (1, 0), (1, 1)]
            for di, dj in vizinhos:
                ni, nj = i + di, j + dj
                if 0 <= ni < linhas and 0 <= nj < colunas:
                    if garden[ni][nj] == "*":
                        qtd_flores += 1
            if qtd_flores == 0:
                continue
            else:
                garden[i][j] = str(qtd_flores)
    garden = ["".join(row) for row in garden]
    return garden              