import sys

messaggio_benvenuto = """
Benvenuto nel quiz di Phyton. Il quiz si compone di 5 domande.
Per ogni domanda potrai scegliere tra quattro opzioni. Inserisci il numero della risposta che reputi corretta.
Per ogni domanda corretta riceverai un punto, in caso di risposta errata non riceverai alcun punto.
Alla fine scoprirai che punteggio hai ottenuto.
Puoi uscire in ogni momento digitandi 'esc'.
"""

print(messaggio_benvenuto)

Contatore_punteggio = 0
while True:
    
    risposta_1 = input("Quale di questi valori rappresenta un valore bool?\n1. ON e OFF \n2. 1 e 0 \n3. True e False \n4. true e false\n")
    if  risposta_1 == "esc":
        print("Arrivederci")
        sys.exit()    
    elif risposta_1 == "3":
        print("La risposta è corretta\n")
        Contatore_punteggio += 1
    else:
        print("Risposta sbagliata, i valori bool sono True e False\n")

    risposta_2 = input("Come si esegue un'operazione di elevamento a potenza?\n1. ** \n2. * \n3. % \n4. //\n")
    if  risposta_2 == "esc":
        print("Arrivederci")
        sys.exit() 
    elif risposta_2 == "1":
        print("La risposta è corretta\n")
        Contatore_punteggio += 1
    else:
        print("Risposta sbagliata, per l'elevamento a potenza si utilizza **\n")

    risposta_3 = input("Quali di questi non è un valore numerico?\n1. 3.0 \n2. 67 \n3. 0.87 \n4. '2'\n")
    if  risposta_3 == "esc":
        print("Arrivederci")
        sys.exit() 
    elif risposta_3 == "4":
        print("La risposta è corretta\n")
        Contatore_punteggio += 1
    else:
        print("Risposta sbagliata, i valori numerici non sono mai tra virgolette\n")

    risposta_4 = input("Quale di questi non è un metodo?\n1. len(variabile) \n2. variabile.upper() \n3. variabile.title() \n4. variabile.capitalize()\n")
    if  risposta_4 == "esc":
        print("Arrivederci")
        sys.exit() 
    elif risposta_4 == "1":
         print("La risposta è corretta\n")
         Contatore_punteggio += 1
    else:
        print("Risposta sbagliata, len(variabile) non è un metodo, ma una funzione\n")

    risposta_5 = input("Quale di questa è una lista?\n1. mylist = {1,2,'ciao'} \n2. mylist = [1,2,'ciao'] \n3. mylist = {'ciao':1, 'hola':2} \n4. my list = ('ciao', 'hola', 1)\n")
    if  risposta_5 == "esc":
        print("Arrivederci")
        sys.exit() 
    elif risposta_5 == "2":
        print("La risposta è corretta\n")
        Contatore_punteggio += 1
    else:
        print("Risposta sbagliata, mylist = [1,2,'ciao'] è una lista\n")
    break


print(f'Il punteggio che hai totalizzato è: {Contatore_punteggio}')
if Contatore_punteggio == 5:
    print("Congratulazioni hai risposto correttamente a tutte domande\n", chr(0x2B50)*5)
elif Contatore_punteggio == 4:
    print("Molto bravo hai risposto correttamente a 4 domande\n", chr(0x2B50)*4)
elif Contatore_punteggio == 3:
    print("Hai risposto correttamente a 3 domande\n", chr(0x2B50)*3)
elif Contatore_punteggio == 2:
    print("Male. Dovresti fare un rispasso. Hai risposto correttamente a 2 domande\n", chr(0x2B50)*2)
elif Contatore_punteggio == 1:
    print("Molto male. Hai risposto correttamente solo a 1 domanda\n", chr(0x2B50)*1)
elif Contatore_punteggio == 0:
    print("Mi dispiace ma hai fallito il test non hai risposto correttamente a nessuna domanda\n", chr(0x1F616)*5)

    
