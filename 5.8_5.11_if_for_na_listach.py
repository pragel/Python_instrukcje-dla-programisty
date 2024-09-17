#powitanie uzytkowników z wyróżnieniem admina
users = ['dawid','admin', 'tomek', 'patrycja', 'maja']
if users:
    for user in users:
        if user == 'admin':
            print(f"Witaj {user.title()} chcesz utworzyć nowy raport?")
        else:
            print(f'{user.title()} dzięki że ponownie się zalogowałeś')
        
else:
    print('Brak użytkowników musimy ich znaleźć :)')
print('\n')
#sprawdzanie czy dany uzytkownik juz istnieje    
user = ['dawid','admin', 'tomek', 'patrycja', 'maja']
new_user = ['monika', 'pawel', 'jacek', 'dawid', 'justyna']

for n_user in new_user:
    if n_user in user:
        print(f'Nazwa użytkownika: {n_user.title()} jest już zajęta. Wybierz inną!!!')
    else:#elif n_user != user:
        print(f'Witaj nowy uzytkowniku {n_user.title()}')
print('\n')
        
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(number)
#wyswietlanie liczb porządkowych od 1 do 9
for numbers in number:
    if numbers == 1:
        print(f'{numbers}st')
    elif numbers == 2:
        print(f'{numbers}nd')
    elif numbers == 3:
        print(f'{numbers}rd')
    else:
        print(f'{numbers}th')
