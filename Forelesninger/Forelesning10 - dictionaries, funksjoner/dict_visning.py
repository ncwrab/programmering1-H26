# Oppretter en dictonary, her med 3 key:value-par
brettspill = {
    'tittel' : 'Dixit',
    'spilletid' : 30,
    'aldersgrense' : 8,
}
# Skriver ut lista
print(brettspill)
print()

# Skriver ut verdien som tilhører en enkelt nøkkel/key
print(brettspill['spilletid'])
print()

# Endrer på verdien som tilhører nøkkelen 'spilletid'
brettspill['spilletid'] = 40
print(brettspill)
# Alternativt kan man endre verdien slik:
brettspill.update({'spilletid' : 20})
print(brettspill)

# Kan også bruke get()-metoden for å hente ut en verdi
print(brettspill.get('spilletid'))

# Legger til et nytt key:value-par. 'beskrivelse' blir nøkkelen/key og verdien/value blir "Give the perfect...osv"
brettspill['beskrivelse'] = "Give the perfect clue so most (not all) players guess the right surreal image card."
print(brettspill)
# Alternativt kunne man lagt det til slik:
# brettspill.update({'beskrivelse' : "Give the perfect clue so most (not all) players guess the right surreal image card."})

# Sletter paret med nøkkelen 'beskrivelse'
brettspill.pop('beskrivelse')
print(brettspill)

# Kan også bruke del for å slette et par, denne gangen paret med nøkkelen 'aldersgrense'
del brettspill['aldersgrense']
print(brettspill)
