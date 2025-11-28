
def mostrar_pares():
    print("\nPares usando FOR:")
    for n in range(1, 101):
        if n % 2 == 0:
            print(n)

    print("\nPares usando WHILE:")
    n = 1
    while n <= 100:
        if n % 2 == 0:
            print(n)
        n += 1
