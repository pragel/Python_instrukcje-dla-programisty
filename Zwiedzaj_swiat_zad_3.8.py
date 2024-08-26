
# wakacje 5 państw do których chciałbym jechać
wakacje = ['włochy', 'zanzibar', 'hiszpania', 'grecja', 'meksyk']
print(wakacje) # wyswietlenie listy
print(sorted(wakacje)) # sortowanie listy alfabetycznie i wyświetlenie jej
print(wakacje) # wyswietlenie znów listy pokazując że sortowanie za pomocą metody sorted było tylko tymczasowe

wakacje.reverse() # odwrócona kolejność listy
print(wakacje)
wakacje.reverse() # użycie drugi raz metody reverse zadziałą tak że lista powróci do swojej orginalnej kolejności
print(wakacje)

wakacje.sort() #stałe posortowanie listy alfabetycznie, przy metodzie sort nie wrócimy do orginalnego układu listy
print(wakacje)
wakacje.sort(reverse = True) # sortowanie odwrotnie alfabetycznie
print(wakacje)
