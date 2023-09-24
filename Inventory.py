def addToInventory(inventory, addedItems):
    total_items = 0
    for item in addedItems:
        if item in inventory.keys():
            for key in inventory.keys():
                if key == item:
                    inventory[key] += 1
                else:
                    break
        else:
            inventory.setdefault(item, 1)

    total_items += sum(inventory.values())
    for k,v in inventory.items():
        print(f'{k} {v}',end='\n')
    return f'total of items is: {total_items}'


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print(addToInventory(inv, dragonLoot))

'''
this is result
45 gold coin
1 rope
1 ruby
1 dagge 
'''
