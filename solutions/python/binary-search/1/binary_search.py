def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")
    lista_original = search_list.copy()
    index_meio = len(search_list) // 2
    while search_list[index_meio] != value:
        if search_list[index_meio] > value:
            search_list = search_list[0:index_meio]
            index_meio = len(search_list) // 2
        elif search_list[index_meio] < value:
            search_list = search_list[index_meio:len(search_list)]
            index_meio = len(search_list) // 2
        else:
            break
    if search_list[index_meio] == value:
        return lista_original.index(value)