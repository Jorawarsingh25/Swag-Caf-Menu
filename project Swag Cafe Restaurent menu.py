menu={
    'Pizza': 100,
    'Burger': 50,
    'Cofee': 30,
    'Tea': 20,
    'Samosa': 20,
    'Poha': 15


}
print('**********Welcome to Swag Cafe**********')
print("Pizza: 100\nBurger: 50\nCofee: 30\nTea: 20\nSamosa: 20\nPoha: 15\n")

total_order=0
user_item=input('Please Enter the your Item..:')

if user_item in menu:
    total_order +=menu[user_item]
    print(f'your item has been add {user_item}')
else:
    print(f'Your item {user_item} has been not available in these Cafe...')
  
another_order=input('Are you interest any other order y/n..?: ')
if another_order=='y':
    user_item2=input('Please enter your any other item: ')

    if user_item2 in menu:
        total_order +=menu[user_item2]
        print(f'your order {user_item2} has been add..')
    else:
        print(f'your order{user_item2} has been not available')

print(f'your total amount is your item to pay {total_order}')