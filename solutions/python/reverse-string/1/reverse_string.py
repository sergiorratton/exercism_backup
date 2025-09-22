def reverse(text):
    lista_nova = []
    for char in text:
        lista_nova.insert(0, char)
    str_final = ""
    for item in lista_nova:
        str_final += item
    return str_final