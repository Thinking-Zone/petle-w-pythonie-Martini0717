pada = False
licznik_nie = 0
while not pada:
    print("Nie pada! yaaay")
    odpowiedz = input("Czy pada? (tak/nie) ")
    if odpowiedz == 'nie':
        licznik_nie += 1
    elif odpowiedz == 'tak':
        print(f"Gyattdamn that sucks, you said 'nie' {licznik_nie} times.")
        pada == True
    elif odpowiedz == 'niewiem':
        print("To wyjdź i się dowiedz xddd")
    else:
        print("Chłopie co ty do mnie gadasz")
