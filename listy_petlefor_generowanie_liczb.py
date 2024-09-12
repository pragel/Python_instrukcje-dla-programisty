# wypisanie liczb pokoleji od 1 do 20 pętlą for
for value in range(1,21):
    print(value)
# utworzenie pustej listy milion po czym za pomoca petli for dodanie do niej pokoleji liczb od 1 do miliona
milion = []
for value in range(1,1000001):
    milion = value
# utworzeni listy od 1 do miliona po czym wyświetlenie najmniejszej liczby najwekszej liczby oraz sumy liczb w zbiorze
milion = list(range(1,1000001))
x = min(milion)
y = max(milion)
z = sum(milion)

print(x)
print(y)
print(z)
    
