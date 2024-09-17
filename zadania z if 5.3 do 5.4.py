alien_color = 'zielony'

if alien_color == 'zielony':
    print("zdobyłeś 5 punktów")
if alien_color == 'czerwony':
    print('Zdobyłeś 10 punktów')


if alien_color == 'czerwony':
    print('Masz 5 punktów')
else:
    print('Zabiłeś człowieka przegrywasz')

if alien_color == 'zielony':
    print('Masz 5 punktów')
else:
    print('Zabiłeś człowieka przegywasz')
    
print('\n')
    
alien = 'żółty'    
if alien == 'zielony':
    print('masz 5 punktów')
elif alien == 'czerwony':
    print('masz 10 punktów')
elif alien == 'żółty':
    print('masz 15 punktów')
else:
    print('To był człowiek przegrałeś')
    
#zadanie 5.6
#etapy życia
age = 65
if age < 2:
    print('jesteś niemowlęciem')
elif age >= 2 and age < 4:
    print('jesteś dzieckiem które uczy się chodzić')
elif age >= 4 and age < 13:
    print('jestes dzieckiem')
elif age >= 13 and age < 20:
    print('jestes nastolatkiem')
elif age >= 20 and age < 65:
    print('jesteś dorosły')
elif age >= 65:
    print('jesteś seniorem')
    
#zadanie 5.7
lista_owocow = ['banany', 'gruszki', 'maliny']
if 'banany' in lista_owocow:
    print('naprawde lubisz banany')
if 'jabłka' in lista_owocow:
    print('naprawde lubisz jabłka')
else:
    print('nie lubisz jabłek')
if 'maliny' in lista_owocow:
    print('naprawde lubisz maliny')
