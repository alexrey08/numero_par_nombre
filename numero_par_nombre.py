while True:
    try:
        numero_par = int(input("Introduce un número: "))
        if numero_par % 2 == 0:
            print(f"el numero {numero_par} es par")
        else:
            print(f"el numero {numero_par} es impar")
    except ValueError:
        print("Escucha tontito, pon un numero bueno")