# -*- coding: utf-8 -*-
import random

Witze=["Stehen ein Schaf und ein Rasenmäher auf einer Wiese. Sagt das Schaf: Määääähhhh! Antwortet der Rasenmäher: Du hast mir gar nichts zu befehlen!", "Wie tragen zwei Ostfriesen einen Kleiderschrank?  Der eine trägt den Schrank, der andere sitzt drin und hält die Kleiderbügel fest", "Früher war ich Schulbusfahrer, sagt der Presslufthämmerer, aber ich habe den Lärm einfach nicht mehr ausgehalten!"]


zufallsantworten = ["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ..."]

einWitz = ""

reaktionsantworten = {"witz": einWitz,
                      "hallo": "aber Hallo", 
					  "geht": "Was verstehst du darunter?", 
					  "essen": "Ich habe leider keinen Geschmackssinn :("
					  }
                      
print("Willkommen beim Chatbot")
print("Worüber würden Sie gerne heute sprechen?")
print("Zum beenden einfach 'Tschau' eintippen")
print("")

nutzereingabe = ""
while nutzereingabe != "tschau":
    nutzereingabe = ""
    reaktionsantworten["witz"] = random.choice(Witze)
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage/Antwort: ")
        
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    
    intelligenteAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))
        
    print("")

print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")