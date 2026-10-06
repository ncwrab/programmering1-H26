# En liste der hvert element i lista er en dictionary. Hver dictionary (bortsett fra den på indeks 0) inneholder 2 key:value-par
planeter = [{'navn':'Tilfeldig planet'},
            {'navn': 'Merkur', 'tyngdekraft':3.7},
            {'navn': 'Venus', 'tyngdekraft': 8.87},
            {'navn':'Jorden', 'tyngdekraft': 9.807},
            {'navn': 'Mars', 'tyngdekraft': 3.721},
            {'navn': 'Jupiter', 'tyngdekraft': 24.79},
            {'navn': 'Saturn', 'tyngdekraft':10.44},
            {'navn': 'Uranus', 'tyngdekraft': 8.87},
            {'navn': 'Neptun', 'tyngdekraft': 11.15}
            ]
# definerer en funksjon som skal skrive ut planetene fra en liste
# Funksjonen har 1 parameter, og denne er tenkt å være en liste
# Funksjonen trenger ikke returnere noen verdi
def skriv_ut_planetliste(liste_som_skal_skrives_ut):
    for index, planet in enumerate(liste_som_skal_skrives_ut):
        print(f'{index} - {planet['navn']}')

# definerer en funksjon som skal skrive ut en "fin" overskrift til brukeren
# Funksjonen trenger ikke returnere noen verdi
def skriv_header():
    print("\n ------------------------------------")
    print("-Hva er din vekt på andre planeter?-")
    print("------------------------------------")





#------------------------------------------------
# All kode ovenfor er kun definisjoner av funksjoner og variabler og gjør ikke noe 'synlig' i seg selv
# Under kommer koden som kjøres:

# Variabelen run skal styre while-løkka. Så lenge run er True vil løkka gå om igjen og om igjen

run = True
while run:   # betyr det samme som while run == True

    # " PSEUDOKODE"
    #Skrive ut overskrift
        # Vi kaller funksjonen skriv_header(). Da utføres koden til den funksjonen, slik vi definerte den tidligere
    skriv_header()
    #Skrive ut liste over planeter
        # Vi kaller funksjonen skriv_ut_planetliste(planeter) og sender med lista vår 'planeter' som argument. Da utføres koden til den funksjonen, slik vi definerte den tidligere
    skriv_ut_planetliste(planeter)
    #Ta input med valg fra bruker, og gi tilbakemelding
    planetnummer = int(input('Velg en planet ved å skrive inn et tall:'))
    #Evt. velge tilfeldig planet for brukeren, og gi tilbakemelding

    #ellers bruker vi tallet brukeren skrev inn, og gir tilbakemelding


    #Ta input med brukers vekt på jorden

    # Beregninger

    #Tilbakemeldinger

    #Ta input om avslutning

    #midlertidig:
    break
