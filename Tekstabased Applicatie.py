def begin():
    naam = input("Hallo wat is je naam? ")
    print("\n")
    beginnen = input("Hallo " + naam + ", wil je mijn tekstbased applicatie bespelen? Ja/Nee\n: ")
    if beginnen == "ja":
        een()
    elif beginnen == "nee":
        print("Oke helaas misschien wil je een andere keer terugkomen")
        begin()
    else:
        print("Voer een geldig antwoord in. Ja/Nee")

def af():
    print("Helaas, je bent afgegaan in mijn applicatie en hebt het einde niet bereikt. Wil je het opnieuw proberen? Ja/Nee")
    antwoord = input(":")
    if antwoord == "ja":
        begin
    elif antwoord == "nee":
        print("Oke helaas, je kan altijd opnieuw terugkomen")
    else:
        ("Vul een geldig antwoord in. Ja/Nee")


def een():
    print("Leuk dat je mijn tekstbased applicatie wilt bespelen, laten we beginnen\n\nJe schrikt wakker en je hoort dat er allerlei chaos buiten aan de hand is en je hoort allemaal mensen schreeuwen, wat doe je?\n ")
    print("A: Je gaat zelf op onderzoek uit om te kijken wat er aan de hand is.")
    print("B: Je gaat eerst in je verblijf rondvragen aan andere mensen of hun weten wat er aan de hand is.")
    antwoord = input(": ")
    if antwoord == "a":
        twee()
    elif antwoord == "b":
        drie()
    else:
        print("Voer een geldig antwoord in. A/B")

def twee():
    print("\nJe komt buiten en je ziet allerlei soldaten rennen en gepantserde voertuigen rijden. Je weet dat er een oorlog is uitgebroken wat doe je?\n ")
    print("A: Je gaat zo snel mogelijk terug naar huis om je spullen op te halen zodat je kan vluchten.")
    print("B: Je vraagt aan een van de militaire officieren of je mee mag vechten om je land te beschermen.")
    antwoord = input(": ")
    if antwoord == "a":
        vier()
    elif antwoord == "b":
        print("Je mag helaas niet meevechten van de staat dus je moet gaan vluchten\n")
        zes()
    else:
        print("Voer een geldig antwoord in. A/B")

def drie():
    print("\nJe vraagt aan allerlei mensen rond wat er aan de hand is en het komt er op neer dat er een oorlog is uitgebroken… Wat doe je?\n ")
    print("A: Je pakt je paspoort en je koffer en gaat zo snel mogelijk naar een vliegveld.")
    print("B: Je gaat eerst de mensen in je verblijf veilig stellen.")
    antwoord = input(": ")
    if antwoord == "a":
        zes()
    elif antwoord == "b":
        af() 
    else:
        print("Voer een geldig antwoord in. A/B")

def vier():
    print("\nJe bent thuis aangekomen en pakt je spullen waar ga je heen?\n ")
    print("A: Je gaat richting de stad waar de oorlog is. ")
    print("B: Je gaat naar het vliegveld zodat je naar een ander land kan gaan. ")
    antwoord = input(": ")
    if antwoord == "a":
        af()
    elif antwoord == "b":
        zes()
    else:
        print("Voer een geldig antwoord in. A/B")

def vijf():
    print("\nJe bent thuis aangekomen en pakt je spullen waar ga je heen?\n ")
    print("A: Je gaat richting de stad waar de oorlog is. ")
    print("B: Je gaat naar het vliegveld zodat je naar een ander land kan gaan. ")
    antwoord = input(": ")
    if antwoord == "a":
        af()
    elif antwoord == "b":
        zes()
    else:
        print("Voer een geldig antwoord in. A/B")

def zes():

def negen():

def tien():

def elf():




begin()