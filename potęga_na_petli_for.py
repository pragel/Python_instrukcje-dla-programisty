#potęga wyliczana z pierwszych dziesieciu liczb całkowitych zaczynając od 1 
#wykorzystuje metode range która nam te pierwsze 10 liczb utworzy 
potega = []
for number in range(1,11):
    potegi = number **2
    potega.append(potegi)
print(potega)
