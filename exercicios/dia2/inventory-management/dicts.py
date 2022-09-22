
def create_inventory(items):

    inventory= {}

    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    
    return inventory
    """
    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

def add_items(inventory, items):

    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    
    return inventory
    """
    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """



def decrement_items(inventory, items):

    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1
        else:
            inventory[item] = 0


    return inventory            
    """
    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """



def remove_item(inventory, item):
    
    if item in inventory:
        inventory.pop(item)

    return inventory
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """


def list_inventory(inventory):

    availables = {item:value for (item, value) in inventory.items() if value > 0}

    keys_availables = availables.keys()
    values_availables = availables.values()

    return list(zip(keys_availables, values_availables))
    
    """
    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
