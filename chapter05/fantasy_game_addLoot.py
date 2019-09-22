import fantasy_game_display

def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    return inventory

def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    fantasy_game_display.displayInventory(inv)

if __name__ == "__main__":
    main()
