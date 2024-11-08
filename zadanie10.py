#Napisz program, który stworzy losowanie liczb od 1 do 10 i poprosi użytkownika aby ten spróbował zgadnąć. 
#Niech ten program także liczy ile razy użytkownik zgadł niepoprawnie i poda tą liczbie po wygraniu gry.

import random
lista = [1,2,3,4,5,6,7,8,9,10]
numer = random.choice(lista)
zgaduj = True

przegrane = 0

while zgaduj:
    odpowiedz = input("podaj liczbę od 1 do 10 i zobacz czy wygrasz loterię!")
    if odpowiedz != str(numer):
        przegrane += 1
        print("Nie trafiłeś, spróbuj jeszcze raz.")
    elif odpowiedz == str(numer):
        print(f"Wreszcie trafiłeś! liczba przegranych jest równa {przegrane}.")
        break
