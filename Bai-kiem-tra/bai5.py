smart_phones = [
    {
        'name': 'Iphone12',
        'price': 28000000,
    },
    {
        'name': 'Samsung N10',
        'price': 16000000,
    },
    {
        'name': 'Oppo 93',
        'price': 7500000,
    },
    {
        'name': 'Vsmart',
        'price': 7400000,
    },
    {
        'name': 'Vivo',
        'price': 4200000,
    }
]

name_phone = input('Input name of phone: ')

found = False 
for phone in smart_phones:
    if phone['name'] == name_phone:
        found = True
        print('Price of', name_phone, 'is', phone['price'])
        break
    if not found:
        print('Not found')

budget = int(input('Input your budget: '))
for phone in smart_phones:
    if phone['price'] <= budget:
        print(f"- {phone['name']}: {phone['price']}.")