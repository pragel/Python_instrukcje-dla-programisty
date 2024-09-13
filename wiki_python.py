(wyrażenie).title() #Dodaje wielką litrere do argumentu przypisanego do wyrażenia
** #Jest to działanie potęgowania 
lista = [] #Tworzenie listy w tym przypadku lista jest pusta możemy dodać do niej argumenty
lista.pop() #Ta metoda usuwa ostatni argument z listy
print(f'{lista} moje zdanie') #W tym przypadku możemy wyświetlić argumenty przypisane do wyrażenia
lista.append('dwa') # do danie do końca listy argument dwa
lista.insert(3, 'trzy') #Metoda insert posiada w sobie dwa argumenty pierwszymn określamy miejsce do którego ma dodać do listy a drugi odnośi sie co ma doda do listy 
print(len(lista)) #Funkcja len zwróci nam ilość wyrażeń znajdujących się w liscie 
del lista[] # funkcją del usuniemy wartość z listy jeżeli znamy ich położenie 
print(sorted(lista)) # sortowanie listy alfabetycznie i wyświetlenie jej. Tą funkcją nie zmienimy na stałe kolejności listy
lista.sort() # funkcja sort posortuje nam alfabetycznie listy na stałe 
lista.sort(reverse = True) #sortuje odwrotnie alfabetycznie.
for value in range(1,21): # wypisanie liczb pokoleji od 1 do 20 pętlą for
    print(value)
number = list(range(1,11)) # utworzenie listy z liczbami od 1 do 10
#wycinek listy
players = ["karol", "martyna", "michał", "florian", "ela"]
print(players[1:3]) #wycinek z listy pokaże nam martyna, michał
print(players[:3]) #pomineliśmy pierwszy argument na wycinku listy co za tym idzie lista wyświetli nam się od pierwszej pozycji do trzeciej czyli karol, martyna, michał
print(players[3:]) #analogiczna sytuacja z tym że wycinek zacznie się od florian, ela 

# KROTKA - JEST TO LISTA NIEMODYFIKOWALNA I TWORZYMY JĄ ZA POMOĆĄ NAWIASÓW OKRĄGŁYCH PRZYKJŁAD:
prostokat = (100,50) # jest to KROTKA nie zmodyfikujemy tej listy w żaden sposób / nie dodamy nie odejmiemy nie zmienimy wartości tych elementów
print(prostokat[0]) # wyswietlanie elementów listy odbywa sie tak samo jak przy zwykłej liście 
kolo = (4,) # możemy w KROTCE zdefiniować jeden argument ale aby była nie edytowalna musi zawierać przecinek
kolo = (2,) #krotke można nadpisać ale nie modyfikować 
