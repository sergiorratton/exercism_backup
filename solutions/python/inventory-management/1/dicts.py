"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    lista_tuplas = []
    for obj in items:
        qtd_item_atual = items.count(obj)
        tupla_par_atual = (obj, qtd_item_atual)
        if tupla_par_atual in lista_tuplas:
            del qtd_item_atual
            del tupla_par_atual
            continue
        lista_tuplas.append(tupla_par_atual)
        del qtd_item_atual
        del tupla_par_atual
    dicionario_final = dict(lista_tuplas)
    return dicionario_final
    
def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        valor_item = 0
        if item in inventory:
            valor_item = inventory[item]
            inventory[item] += 1
        else:
            valor_item += 1
            inventory[item] = valor_item
    return inventory
    
        
def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    
    for item in items:
        if item in inventory:
            valor_item = inventory[item]
            inventory[item] -= 1
            if inventory[item] <= 0:
                inventory[item] = 0
    return inventory
    
def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory
    
def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    lista_final = []
    for item in inventory:
        if inventory[item] != 0:
            tupla_atual = (item, inventory[item])
            lista_final.append(tupla_atual)
    return lista_final

