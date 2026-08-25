# Et lite program som skal regne ut hva en brukers vekt vil være på månen.
# Brukeren må her skrive inn sin vekt som en variabel:
my_earth_weight = 100

# Variabler for tyngdekraft på jorden og månen
earth_gravity = 9.807       # Hvilken datatype har disse to variablenes data?
moon_gravity = 1.622

# Formel for å beregne vekten på månen ut fra vekten på jorden.
# Her brukes verdiene som er lagret i variablene våre til å beregne vekten på månen
moon_weight = my_earth_weight / earth_gravity * moon_gravity

# Skriver ut resultatet (brukers vekt på månen)
print(moon_weight)
