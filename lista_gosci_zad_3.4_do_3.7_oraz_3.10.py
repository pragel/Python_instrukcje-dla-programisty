lista_gosci = ['beata', 'patrycja', 'rafał'] #utworzona lista gości 
#zaproszenie gości każdego z osobna po przez wyciągnięcie z listy
print(f"Cześć zapraszam Cię {lista_gosci[0]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[1]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[2]} na obiad\n")
print(lista_gosci)

nieobecny_gosc = lista_gosci.pop() #usuniecie gościa za pomocą metody pop usuwa ona ostatniego gościa z listy chyba że w sobie ma argument pokazujący którą wartość z listy usunąć i przypisanie jej bo chwilowo jeszcze istnieje do wyrażenia nieobecny_gość

print(f"Niestety {nieobecny_gosc.title()}a nie będzię dzisiaj na obiedzie.")

lista_gosci.append('przemek') # dodanie do końca listy gościa
print(lista_gosci)
print(f"Cześć zapraszam Cię {lista_gosci[0]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[1]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[2]} na obiad\n")

print('Hej znalazłem większy stół')

lista_gosci.insert(0,'urszula') # za pomocą metody insert która posiada w sobie dwa argumenty miejsce w które ma dodać do listy oraz wartość którą ma dodać
lista_gosci.insert(2, 'andrzej')
lista_gosci.append('dorota') #append dodaje zawsze na koniec listy

print(f"Cześć zapraszam Cię {lista_gosci[0]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[1]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[2]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[3]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[4]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[5]} na obiad\n")
print(len(lista_gosci)) # funkcja len informuje ile wartości jest w liśćie
print('Niestety stół nie dotarł na czas dlatego też moge zaprosić dwie osoby')
print(f'Przepraszam Cię {lista_gosci.pop()} ale obiad muszę odwołać') # funkcaj w tym przypadku usuwa ostatnią osobę z listy
print(f'Przepraszam Cię {lista_gosci.pop()} ale obiad muszę odwołać')
print(f'Przepraszam Cię {lista_gosci.pop()} ale obiad muszę odwołać')
print(f'Przepraszam Cię {lista_gosci.pop()} ale obiad muszę odwołać\n')
print(len(lista_gosci))
del lista_gosci[1] # funkcją del usuwamy wartości listy jeżeli znamy ich położenie 
del lista_gosci[0]

print(lista_gosci)
