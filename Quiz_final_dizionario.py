def quiz():
    messaggio_benvenuto = """
    Benvenuto nel quiz di Python. Il quiz si compone di 5 domande.
    Per ogni domanda potrai scegliere tra quattro opzioni. Inserisci il numero della risposta che reputi corretta.
    Per ogni domanda corretta riceverai un punto, in caso di risposta errata non riceverai alcun punto.
    Alla fine scoprirai che punteggio hai ottenuto.
    Puoi uscire in ogni momento digitando 'esc'.
    """
    print(messaggio_benvenuto)

    domande = {
        "Quale di questi valori rappresenta un valore bool?": ("1. ON e OFF", "2. 1 e 0", "3. True e False", "4. true e false", "3"),
        "Come si esegue un'operazione di elevamento a potenza?": ("1. **", "2. *", "3. %", "4. //", "1"),
        "Quali di questi non è un valore numerico?": ("1. 3.0", "2. 67", "3. 0.87", "4. '2'", "4"),
        "Quale di questi non è un metodo?": ("1. len(variabile)", "2. variabile.upper()", "3. variabile.title()", "4. variabile.capitalize()", "1"),
        "Quale di questa è una lista?": ("1. mylist = {1,2,'ciao'}", "2. mylist = [1,2,'ciao']", "3. mylist = {'ciao':1, 'hola':2}", "4. my list = ('ciao', 'hola', 1)", "2")
    }

    messaggi_punteggio = {
        5: "Congratulazioni hai risposto correttamente a tutte domande\n" + chr(0x2B50)*5,
        4: "Molto bravo hai risposto correttamente a 4 domande\n" + chr(0x2B50)*4,
        3: "Hai risposto correttamente a 3 domande\n" + chr(0x2B50)*3,
        2: "Male. Dovresti fare un ripasso. Hai risposto correttamente a 2 domande\n" + chr(0x2B50)*2,
        1: "Molto male. Hai risposto correttamente solo a 1 domanda\n" + chr(0x2B50)*1,
        0: "Mi dispiace ma hai fallito il test non hai risposto correttamente a nessuna domanda\n" + chr(0x1F616)*5
    }

    contatore_punteggio = 0

    for domanda, opzioni in domande.items():
        print(domanda)
        for opzione in opzioni[:-1]:
            print(opzione)
        risposta = input("Inserisci il numero della risposta: ")
        
        if risposta == "esc":
            print("Arrivederci")
            return
        elif risposta == opzioni[-1]:
            print("La risposta è corretta\n")
            contatore_punteggio += 1
        else:
            print(f"Risposta sbagliata\n")
    
    print(f'Il punteggio che hai totalizzato è: {contatore_punteggio}')
    print(messaggi_punteggio[contatore_punteggio])

quiz()

