#twierdzenia true or false
car = 'subaru'
print("czy car == 'subaru' ? Przewiduje wartość true")
print(car == 'subaru')

print("czy car == 'mercedes' ? Przewiduje wartość false")
print(car == 'mercedes')

print("czy car == 'Subaru' ? Przewiduje wartość false")
print(car == 'Subaru')

#wielkość liter ma znaczenie
print("czy car == 'Subaru' ? Przewiduje wartość false")
print(car.title() == 'Subaru')

print('\nSprawdzenie czy użytkownik istnieje na liście')
#sprawdzenie czy użytkownik istnieje na liście 
users = ['maria', 'radek', 'mateusz', 'karolina']
print('maria' in users)
print('tomek' in users)

print('\nDziałania na liczbach')

wiek = 18
print('czy karolina ma 18 lat?')
print(wiek == 18)
print('czy karolina ma więcej lat niż 18?')
print(wiek > 18)
print('czy karolina ma mniej lat niż 18?')
print(wiek < 18)

