import random

pada = random.choice([True, False])
zgaduj = True

while zgaduj:
    odpowiedz = input("Czy pada? (t/n) ")
    if (pada == True):
        if odpowiedz == 't':
            print("Masz rację, pada xddd")
        elif odpowiedz == 'n':
            print("nie zgadłeś, pada xddd")
        else:
            print("Kolego masz jakiś problem z czytaniem??")
    elif (pada == False):
        if odpowiedz == 't':
            print("nie zgadłeś, nie pada xddd")
        elif odpowiedz == 'n':
            print("Masz rację, nie pada xddd")
        else:
            print("Kolego masz jakiś problem z czytaniem??")
    break
