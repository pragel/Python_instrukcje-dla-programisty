# wypisanie liczb pokoleji od 1 do 20 pętlą for
for value in range(1,21):
    print(value)
# utworzenie pustej listy milion po czym za pomoca petli for dodanie do niej pokoleji liczb od 1 do miliona
milion = []
for value in range(1,1000001):
    milions = value
    milion.append(milions)
#print(milion)
# utworzeni listy od 1 do miliona po czym wyświetlenie najmniejszej liczby najwekszej liczby oraz sumy liczb w zbiorze
milion = list(range(1,1000001))
x = min(milion)
y = max(milion)
z = sum(milion)

print(x)
print(y)
print(z)



potegi = list(range(3,31,))
for potegowanie in potegi:
    value = potegowanie **3
print(potegi)
print("\n") 
#utworzenie pustej listy i wpisanie do niej liczb od 1 do 10 ale do potęgi 3
szescian = []
for value in range(1,11):
    szesc = value **3
    szescian.append(szesc)
print(szescian)
# ta sama instrukcja tylko krócej zapisana
szescian = []
for value in range(1,11):
    szescian.append(value**3)
print(szescian)
# funkcja składana
szescian = [value **3 for value in range(1,11)]
print(szescian)

#WYCINKI
nieparzyste = list(range(1,20,2))
for nieparzyst in nieparzyste:
    print(nieparzyst)
print("\n")

print("Pierwsze trzy elementy listy to: ")
print(nieparzyste[0:3])
print("Trzy elementy w środku to: ")
print(nieparzyste[4:7])
print("Trzy ostatnie elementy listy to:")
print(nieparzyste[-3:])
