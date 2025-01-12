def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b == 0:
        return "Błąd: Dzielenie przez zero!"
    return a / b

# Menu kalkulatora
def kalkulator():
    print("Wybierz operację:")
    print("1. Dodaj")
    print("2. Odejmij")
    print("3. Pomnóż")
    print("4. Podziel")
    
    wybor = input("Wprowadź numer operacji (1/2/3/4): ")
    
    if wybor in ['1', '2', '3', '4']:
        a = float(input("Wprowadź pierwszą liczbę: "))
        b = float(input("Wprowadź drugą liczbę: "))
        
        if wybor == '1':
            print(f"Wynik: {dodaj(a, b)}")
        elif wybor == '2':
            print(f"Wynik: {odejmij(a, b)}")
        elif wybor == '3':
            print(f"Wynik: {pomnoz(a, b)}")
        elif wybor == '4':
            print(f"Wynik: {podziel(a, b)}")
    else:
        print("Niepoprawny wybór")
