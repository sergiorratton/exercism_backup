def transform(legacy_data):
    data = {}
    for item in legacy_data:
        numero = item
        letras = legacy_data[item]
        for letra in letras:
            letra = letra.lower()
            data[letra] = numero
    data = dict(sorted(data.items()))
    return data
