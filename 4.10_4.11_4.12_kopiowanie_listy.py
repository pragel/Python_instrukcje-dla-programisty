pizza = ['margeritta', 'hawajska', 'cztery sery']

for value in pizza: #wyświetlenie przez pętle listy pizza
    print(value)
   
friend_pizza = pizza[:]#kopiowanie listy pizza

print('\n')

pizza.append('pepperoni') #dodanie kolejnego elementu do listy
friend_pizza.append('capriciosa')#dodanie kolejnego elementu do listy

print("moje ulubione pizze to:")
for value in pizza:
    print(value)
print('\n')
print("kolegi ulubione pizze to:")
for value in friend_pizza:
    print(value)
    
print('\n')    
my_foods = ['pizza', 'falafel', 'ciasto z marchwi']

you_foods = my_foods[:]

my_foods.append('makaron')
you_foods.append('krupnik')

for value in my_foods:
    print(value)
    
print('\n')

for value in you_foods:
    print(value)
