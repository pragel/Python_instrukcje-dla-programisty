lista_gosci = ['beata', 'patrycja', 'rafał']
print(f"Cześć zapraszam Cię {lista_gosci[0]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[1]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[2]} na obiad\n")
print(lista_gosci)

nieobecny_gosc = lista_gosci.pop()

print(f"Niestety {nieobecny_gosc.title()}a nie będzię dzisiaj na obiedzie.")

lista_gosci.append('przemek')
print(lista_gosci)
print(f"Cześć zapraszam Cię {lista_gosci[0]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[1]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[2]} na obiad\n")

print('Hej znalazłem większy stół')

lista_gosci.insert(0,'urszula')
lista_gosci.insert(2, 'andrzej')
lista_gosci.append('dorota')

print(f"Cześć zapraszam Cię {lista_gosci[0]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[1]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[2]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[3]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[4]} na obiad")
print(f"Cześć zapraszam Cię {lista_gosci[5]} na obiad\n")

print('Niestety stół nie dotarł na czas dlatego też moge zaprosić dwie osoby')
print(f'Przepraszam Cię {lista_gosci.pop()} ale obiad muszę odwołać')
print(f'Przepraszam Cię {lista_gosci.pop()} ale obiad muszę odwołać')
print(f'Przepraszam Cię {lista_gosci.pop()} ale obiad muszę odwołać')
print(f'Przepraszam Cię {lista_gosci.pop()} ale obiad muszę odwołać\n')

del lista_gosci[1]
del lista_gosci[0]

print(lista_gosci)
