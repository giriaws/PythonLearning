
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry','lint']


for k,v in inventory.items():
    if k=='backpack':
        inventory['backpack']=sorted(inventory['backpack'])

    
print("new inventory:",inventory)   

#remove dagger

for k,v in inventory.items():
    if k=='backpack':
        if 'dagger' in inventory['backpack']:
            inventory['backpack'].remove('dagger')

print("after remove:",inventory)

# Add 50
inventory['gold'] = inventory.get('gold')+50

print(inventory)

