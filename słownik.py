person = {
    'first_name' : 'dawid',
    'last_name' : 'janicki',
    'age' : '29',
    'city' : 'częstochowa',
}
print(person)

lucky_number = {
    'dawid' : '7',
    'patrycja' : '11',
    'daniel' : '3',
    'karol' : '1',
    "piotr" : '15',
}

print(f"Ulubiona liczba Dawida to {lucky_number['dawid']}")
print(f"Ulubiona liczba Patrycji to {lucky_number['patrycja']}")
print(f"Ulubiona liczba Daniela to {lucky_number['daniel']}")
print(f"Ulubiona liczba Karola to {lucky_number['karol']}")
print(f"Ulubiona liczba Piotrka to {lucky_number['piotr']}")

glosariusz = {
    'del_lista' : 'Usuniemy nią wartość jeżeli znamy jej położenie',
    'wyrazenie.title()' : 'Zaczyna argument z wielkiej litery ',
    'lista.pop()' : 'usuwa ostatni argument z listy'
    'krotka' : 'Używamy gdy nie chcemy aby lista była modyfikowalna i tworzymy ją z nawiasów okrągłych'
    'len(lista)' : 'zwróci nam ilość elementów w liście'
}

print("Glosariusz to taki krótki słownik\n")
print(f"Jeżeli nie wisz co zrobi funkcja 'del lista' to już wyjaśniam Ci to poniżej\n{glosariusz['del_lista']}")
print(f"Gdybyś jednak przeoczył funkcje '.title()' to lece z pomocom i wyjaśniam{glosariusz['wyrazenie.title()']}")
print(f"Nie mów że nie umiesz usuwać ostatniego argumentu z listy...\nno cóż lece z pomocą{glosariusz['lista.pop()']}")
print(f"hmmm jeżeli zastanawiałeś się co to jest krótka ahh sorki krotka to cyk prosze mówisz i masz\n{glosariusz['krotka']} ")
print(f'To już koniec lekcji na dziś ale zobaczmy jeszcze funkcje len\n {}')
