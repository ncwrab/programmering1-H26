# Lager en ny liste med navn på planeter. Listen inneholder 6 elementer (6 planeter):
planeter = ["Merkur", "Venus", "Jorden", "Jupiter", "Saturn", "Uranus"]
print(planeter) # Skriver ut alle elementer i listen

# For å skrive ut ett enkeltelement kan vi gjøre det på følgende måte. Tallet i firkantparentesen er indeksnummer
print(planeter[0])
# NB! Merk at alle lister starter på indeksnummer 0. Altså, det første elementet i lista vil alltid ha indeksnummer 0 ( IKKE 1!)

# Ønsker vi å endre et spesifikt element i listen kan vi gjøre det som under. Under endrer vi elementet med indeksnummer 4 til å være "Mars"
# Dette vil endre det femte elementet i lista (0, 1, 2, 3, 4 <- nr fem når vi starter å telle på 0)
planeter[4] = "Mars"
print(planeter)

# For å legge til elementer kan vi bruke .append(). Merk at denne metoden legger til elementet bakerst i lista
planeter.append("Neptune")
print(planeter)
planeter.append("Pluto")
print(planeter)

# Vi kan også bruke .insert() for å legge til elementer. Denne metoden krever at vi har med indeksnummeret der vi vil legge inn elementet, samt hva 'verdien' skal være
planeter.insert(3, "Saturn")
print(planeter)
planeter.insert(3, "Tellus")
print(planeter)

# Vi kan bruke .pop() for å fjerne et element fra listen. .pop() fjerner det bakerste elementet i listen
planeter.pop()
print(planeter)
# Vi kan også bruke .pop() for å fjerne et element på et spesifikt indeksnummer:
planeter.pop(3)
print(planeter)

# Vi legger til nok et element i lista (bakerst) med verdien 'Saturn'. Etter dette vil lista inneholde 2 elementer med verdien 'Saturn'
planeter.append("Saturn")
print(planeter)

# Hvis vi ikke kjenner indeksnummeret, men vi kjenner verdien til et element, kan vi bruke .remove() for å fjerne det
# Merk at .remove() kun fjerner den første forekomsten av verdien, slik at det fortsatt fins et element bakerst i lista med verdi 'Saturn':
planeter.remove("Saturn")
print(planeter)

# Hvis vi ønsker en sortert liste til midlertidig bruk kan vi bruke sorted(). sorted() lager en kopi av lista:
print("Midlertidig sortert liste:")
print(sorted(planeter))
# Merk at den originale lista ikke er sortert, siden det kun ble laget en separat kopi over
print(" Den originale lista")
print(planeter)

# Dersom vi ønsker å reversere rekkefølgen på elementene i lista, uten å sortere dem, kan vi bruke .reverse():
planeter.reverse()
print(planeter)

# .sort() sorterer lista vår alfabetisk, og denne gangen er endringen/sorteringen permanent:
planeter.sort()
print(planeter)

# .sort() kan også gi oss en reversert sortert liste direkte ved å benytte den slik: (lista sorteres først, så reverseres):
planeter.sort(reverse=True)
print(planeter)
