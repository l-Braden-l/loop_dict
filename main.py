#Braden Leach
#January 28 2024
#Looping Dictionary




#---Looping Dictionary---#
mounatains = {
        'Andes': 6962,
        'Rockies': 4401,
        'Urals': 1895,
        'Alps': 4807,
        'Himalayas': 8848
}

#---Items---#
for key,value in mounatains.items():
    print(f'The {key} have a height of {value} meters tall!\n')

#---Keys---#
for key in mounatains.keys():
    print(key)
#---Values---#
for value in mounatains.values():
    print(value)