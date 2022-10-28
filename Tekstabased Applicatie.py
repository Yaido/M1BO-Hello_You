import os, time, sys

def pprint(msg):
    for letter in msg:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
    print('\n')

def begin():
    while True:
        os.system('cls')
        naam = input("Hallo wat is je naam? ")
        pprint("\n")
        beginnen = input("Hallo " + naam + ", wil je mijn tekstbased applicatie bespelen? Ja/Nee\n: ")
        if beginnen == "ja":
            een()
        elif beginnen == "nee":
            pprint("Oke helaas misschien wil je een andere keer terugkomen")
            begin()
        else:
            pprint("Voer een geldig antwoord in. Ja/Nee")

def af():
    while True:
        pprint("Helaas, je bent afgegaan in mijn applicatie en hebt het einde niet bereikt. \nWil je het opnieuw proberen? Ja/Nee")
        antwoord = input(":")
        if antwoord == "ja":
            begin()
        elif antwoord == "nee":
            pprint("Oke helaas, je kan altijd opnieuw terugkomen")
            begin()
        else:
            ("Vul een geldig antwoord in. Ja/Nee")

def einde():
    while True:
        pprint("Hallo, je hebt een einde gevonden in mijn tektstbased applicatie\nMaar er zijn meerdere einden")
        antwoord = input("Zou je het opnieuw willen proberen? Ja/Nee")
        if antwoord == "ja":
            begin()
        elif antwoord == "nee":
            pprint("Oke helaas dat je het niet nog een keer wilt proberen.")
        else:
            pprint("Voer een geldig antwoord in. Ja/Nee")


def een():
    while True:
        os.system('cls')
        pprint("Leuk dat je mijn tekstbased applicatie wilt bespelen, laten we beginnen. LET OP: Deze tekstbased applicatie is hoofdlettergevoelig, dus geen hoofdletters gebruiken!\n\nJe schrikt wakker en je hoort dat er allerlei chaos buiten aan de hand is en je hoort allemaal mensen schreeuwen, wat doe je?\n ")
        pprint("A: Je gaat zelf op onderzoek uit om te kijken wat er aan de hand is.")
        pprint("B: Je gaat eerst in je verblijf rondvragen aan andere mensen of hun weten wat er aan de hand is.")
        antwoord = input(": ")
        if antwoord == "a":
            twee()
        elif antwoord == "b":
            drie()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def twee():
    while True:    
        os.system('cls')
        pprint("\nJe komt buiten en je ziet allerlei soldaten rennen en gepantserde voertuigen rijden. Je weet dat er een oorlog is uitgebroken wat doe je?\n ")
        pprint("A: Je gaat zo snel mogelijk terug naar huis om je spullen op te halen zodat je kan vluchten.")
        pprint("B: Je vraagt aan een van de militaire officieren of je mee mag vechten om je land te beschermen.")
        antwoord = input(": ")
        if antwoord == "a":
            vier()
        elif antwoord == "b":
            pprint("Je mag helaas niet meevechten van de staat dus je moet gaan vluchten\n")
            zes()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def drie():
    while True:
        os.system('cls')
        pprint("\nJe vraagt aan allerlei mensen rond wat er aan de hand is en het komt er op neer dat er een oorlog is uitgebroken… Wat doe je?\n ")
        pprint("A: Je pakt je paspoort en je koffer en gaat zo snel mogelijk naar een vliegveld.")
        pprint("B: Je gaat eerst de mensen in je verblijf veilig stellen.")
        antwoord = input(": ")
        if antwoord == "a":
            zes()
        elif antwoord == "b":
            pprint("De soldaten waren het bedrijf binnengevallen en je bent af gegaan")
            af() 
        else:
            pprint("Voer een geldig antwoord in. A/B")

def vier():
    while True:
        os.system('cls')
        pprint("\nJe bent thuis aangekomen en pakt je spullen waar ga je heen?\n ")
        pprint("A: Je gaat richting de stad waar de oorlog is. ")
        pprint("B: Je gaat naar het vliegveld zodat je naar een ander land kan gaan. ")
        antwoord = input(": ")
        if antwoord == "a":
            af()
        elif antwoord == "b":
            zes()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def zes():
    while True:
        os.system('cls')
        pprint("\nJe bent op het vliegveld aangekomen en het is heel druk, welk vliegtuig pak je?\n ")
        pprint("A: Je pakt het vliegtuig naar de Verenigde Staten maar de kans dat je die mist is 80%")
        pprint("B: Je pakt het vliegtuig naar Nederland en die kan je niet missen")
        antwoord = input(": ")
        if antwoord == "a":
            pprint("Je hebt helaas het vliegtuig gemist… Pak die naar Nederland")
            zes()
        elif antwoord == "b":
            negen()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def negen():
    while True:
        os.system('cls')
        pprint("\nJe bent in Nederland aangekomen wat doe je?\n ")
        pprint("A. Je gaat met je groep mee naar het AZC")
        pprint("B. Je gaat je eigen weg volgen en kijkt wel wat er gebeurd")
        antwoord = input(": ")
        if antwoord == "a":
            tien()
        elif antwoord == "b":
            pprint("\nJe hebt geen geld dus bent niet ver gekomen.\n")
            af()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def tien():
    while True:
        os.system('cls')
        pprint("\nJe bent aangekomen in het AZC en je krijgt 2 opties toegewezen wat doe je?\n ")
        pprint("A. Je krijgt aangeboden de taal te leren.")
        pprint("B. Je krijgt een saaie baan aangeboden om weinig geld te verdienen")
        antwoord = input(": ")
        if antwoord == "a":
            elf()
        elif antwoord == "b":
            twaalf()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def elf():
    while True:
        os.system('cls')
        pprint("\nJe krijgt je eerste les in taal, je hebt wat vrienden gemaakt wat doe je?\n ")
        pprint("A. Je gaat naar huis om de taal te leren")
        pprint("B. Je gaat met je vrienden naar buiten om wat te doen")
        antwoord = input(": ")
        if antwoord == "a":
            dertien()
        elif antwoord == "b":
            veertien()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def twaalf():
    while True:
        os.system('cls')
        pprint("\nOke, je bent gaan werken maar het blijkt saai en niet leuk werk te zijn voor weinig geld wat doe je?\n ")
        pprint("A. Je gaat toch de taal goed leren")
        pprint("B. Je hebt wat connecties gemaakt in Nederland en gaat de criminaliteit in")
        antwoord = input(": ")
        if antwoord == "a":
            elf()
        elif antwoord == "b":
            vijftien()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def dertien():
    while True:
        os.system('cls')
        pprint("\nJe bent naar huis gegaan om de taal te leren en je hebt al wat kennis over een paar woordjes, en je krijgt een baan aangeboden wat doe je?\n ")
        pprint("A. Je slaat de baan nog even af en leert de taal beter zodat je eventueel kan gaan studeren")
        pprint("B. Je gaat werken bij de Supermarkt als vakkenvuller")
        antwoord = input(": ")
        if antwoord == "a":
            negentien()
        elif antwoord == "b":
            twaalf()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def veertien():
    while True:
        os.system('cls')
        pprint("\nJe bent naar buiten gegaan met je vrienden en blijkt dat je vrienden in de drugs zitten wat doe je?\n ")
        pprint("A. Je gaat met hun mee en kijkt wat het je brengt")
        pprint("B. Je gaat direct naar huis en spreekt hun niet meer")
        antwoord = input(": ")
        if antwoord == "a":
            vijftien()
        elif antwoord == "b":
            zestien()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def vijftien():
    while True:
        os.system('cls')
        pprint("\nEenmaal in de criminaliteit aangekomen heb je je eigen taak gekregen wat doe je?\n ")
        pprint("A. Je gaat de stad in en zoekt wat mensen die je spul willen kopen.")
        pprint("B. Je besluit het toch niet te doen en gaat naar huis")
        antwoord = input(": ")
        if antwoord == "a":
            zeventien()
        elif antwoord == "b":
            zestien()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def zestien():
    while True:
        os.system('cls')
        pprint("\nJe hebt een goede keuze gemaakt en besluit niet meer met hun om te gaan dus je gaat maar verder met de taal wat nu?\n ")
        pprint("A. Volgende dag ga je op zoek of je een bijbaantje kan vinden")
        pprint("B. Volgende dag ga je gewoon weer naar de taalles")
        antwoord = input(": ")
        if antwoord == "a":
            achttien()
        elif antwoord == "b":
            negentien()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def zeventien():
    while True:
        os.system('cls')
        pprint("\nJe bent je eerste klant tegengekomen, hij heeft je betaald wat doe je?\n ")
        pprint("A. Je gaat terug naar je leverancier om meer te halen en het geld te leveren")
        pprint("B. Je gaat nog meer verkopen totdat alles op is en je niks meer hebt")
        antwoord = input(": ")
        if antwoord == "a":
            twintig()
        elif antwoord == "b":
            eenentwintig()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def achttien():
    while True:
        os.system('cls')
        pprint("\nJe bent opzoek gegaan naar een bijbaantje en je bent bij de supermarkt aangekomen wat doe je?\n ")
        pprint("A. Je gaat gelijk vragen of je kan solliciteren in de winkel")
        pprint("B. Je gaat online kijken naar eventuele vacatures van winkels")
        antwoord = input(": ")
        if antwoord == "a":
            tweeentwintig()
        elif antwoord == "b":
            drieentwintig()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def negentien():
    while True:
        os.system('cls')
        pprint("\nJe bent weer bij de taalles wat doe je?\n ")
        pprint("A. Je vraagt of je leraar niet een klusje voor je heeft om wat bij te verdienen.")
        pprint("B. Je gaat weer terug naar huis en je doet elke dag hetzelfde totdat je werk hebt gevonden en een carrière bent gestart.")
        antwoord = input(": ")
        if antwoord == "a":
            vierentwintig()
        elif antwoord == "b":
            einde()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def twintig():
    while True:
        os.system('cls')
        pprint("\nJe bent bij je leverancier maar hij is boos dat je niet alles hebt verkocht en wilt je geen nieuw spul geven totdat alles is verkocht\n ")
        pprint("A. Je gaat weer verkopen totdat alles op is")
        pprint("B. Je besluit toch nog om alles in te leveren omdat je het niet vertrouwd en naar de taalles te gaan")
        antwoord = input(": ")
        if antwoord == "a":
            vijfentwintig()
        elif antwoord == "b":
            zestien()
        else:
            pprint("Voer een geldig antwoord in. A/B")  

def eenentwintig():
    while True:
        os.system('cls')  
        pprint("\nJe hebt alles verkocht wat doe je nu?\n ")
        pprint("A. Je gaat naar je leverancier geld brengen en nieuw spul ophalen")
        pprint("B. Je besluit al het geld zelf te houden en naar taalles te gaan")
        antwoord = input(": ")
        if antwoord == "a":
            vijfentwintig()
        elif antwoord == "b":
            pprint("\nJe leverancier kwam je opzoeken en je bent afgeschoten door hem\n")
            af()
        else:
            pprint("Voer een geldig antwoord in. A/B") 

def tweeentwintig():
    while True:
        os.system('cls')
        pprint("\nJe bent in de winkel gaan solliciteren en je bent aangenomen wat doe je?\n ")
        pprint("A. Je gaat jezelf gelijk inroosteren voor de week wanneer je tijd hebt")
        pprint("B. Je gaat eerst jezelf focussen op taalles en wat bijverdienen bij de winkel")
        antwoord = input(": ")
        if antwoord == "a":
            zevenentwintig()
        elif antwoord == "b":
            achtentwintig()
        else:
            pprint("Voer een geldig antwoord in. A/B") 

def drieentwintig():
    while True:
        os.system('cls')
        pprint("\nJe bent uitgekomen op een winkel vlakbij jou huis en bent aangenomen wat doe je?\n ")
        pprint("A. Je gaat jezelf gelijk inroosteren voor de week wanneer je tijd hebt")
        pprint("B. Je gaat eerst jezelf focussen op taalles en wat bijverdienen bij de winkel")
        antwoord = input(": ")
        if antwoord == "a":
            zevenentwintig()
        elif antwoord == "b":
            achtentwintig()
        else:
            pprint("Voer een geldig antwoord in. A/B")

def vierentwintig():
    os.system('cls')
    pprint("\nJe leraar heeft helaas geen klusje voor je en zegt dat je je eerst moet focussen op de taal.\n ")
    einde()

def vijfentwintig():
    os.system('cls')
    pprint("\nJe bouwt een goede band op met je leverancier, maar uiteindelijk word je doodgemaakt door hem, hij was niet te vertrouwen.\n")
    einde()

def zevenentwintig():
    os.system('cls')
    pprint("\nJe hebt een goede carrière opgebouwd en blijft jezelf focussen op je taal en krijgt goed werk!\n")
    einde()

def achtentwintig():
    os.system('cls')
    pprint("\nNadat je bent geslaagd voor je taal en je de taal volledig kent ben je wat gaan doen wat je leuk vind en bent succesvol geworden in nederland!	\n")
    einde()

begin()