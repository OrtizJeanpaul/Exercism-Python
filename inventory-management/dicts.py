"""Functions to keep track and alter inventory."""


def create_inventory(items):
    result = {}

    for _, word in enumerate(items):
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1
    
    return result



def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for _, word in enumerate(items):
        if word in inventory:
            inventory[word] = inventory[word] + 1
        else:
            inventory[word] = 1
    
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """


    for _, word in enumerate(items):
        if word in inventory and inventory[word] > 0:
            inventory[word] = inventory[word] - 1
    
    return inventory
    

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        del inventory[item]

    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inv_list = []
    for key in inventory:
        if inventory[key] > 0:
            inv_list.append((key, inventory[key]))

    return inv_list