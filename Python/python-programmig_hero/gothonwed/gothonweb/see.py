#??
africa = {
    "South Africa": 'SA',
    "Nigeria": "NG",
    "Kenya":'KY',
    'Ethiopia': "ET"
}

cities = {
    'SA':'Soweto',
    'KY': 'Nairobi'
}

cities['NG'] = 'Nigeria city'
cities['ET'] = 'King Salasia'

print('-'*10)
print("NG has city", cities['NG'])
print("ET has city", cities['ET'])

print('-'*10)
print("South Africa is Abbreviated as ", africa['South Africa'])
print("Kenya is Abbreviated as ", africa['Kenya'])
print("Nigeria is Abbreviated as ", africa['Nigeria'])
print("Ethiopia is Abbreviated as ", africa['Ethiopia'])

print('-'*10)
for city, abbrev in list(cities.items()):
    print(f'{city} - has city {abbrev}')

print('-'*10)
for african, abbrev in list(africa.items()):
    print(f'{african} is abbreviated as {abbrev}')
    print(f'and has city {cities[abbrev]}')
    print('-'*10)