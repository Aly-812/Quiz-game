#Domende da 1 a 3
messaggio_benvenuto = """
Benvenuto nel quiz di Phyton. Il quiz si compone di 5 domande.
Per ogni domanda potrai scegliere tra quattro opzioni. Inserisci il numero della risposta che reputi corretta.
Per ogni domanda corretta riceverai un punto, in caso di risposta errata non riceverai alcun punto.
Alla fine scoprirai che punteggio hai ottenuto.
"""

print(messaggio_benvenuto)


Contatore_punteggio = 0

risposta_1 = input("Quale di questi valori rappresenta un valore bool?\n1. ON e OFF \n2. 1 e 0 \n3. True e False \n4. true e false\n")
if risposta_1 == "3":
    print("La risposta è corretta\n")
    Contatore_punteggio += 1
else:
    print("Risposta sbagliata, i valori bool sono True e False\n")

risposta_2 = input("Come si esegue un'operazione di elevamento a potenza?\n1. ** \n2. * \n3. % \n4. //\n")
if risposta_2 == "1":
    print("La risposta è corretta\n")
    Contatore_punteggio += 1
else:
    print("Risposta sbagliata, per l'elevamento a potenza si utilizza **\n")

risposta_3 = input("Quali di questi non è un valore numerico?\n1. 3.0 \n2. 67 \n3. 0.87 \n4. '2'\n")
if risposta_3 == "4":
    print("La risposta è corretta\n")
    Contatore_punteggio += 1
else:
    print("Risposta sbagliata, i valori numerici non sono mai tra virgolette\n")
