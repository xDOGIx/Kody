import math

def pole_koła(r):
    return math.pi*r**2

def pole_kwadratu(y):
    return y**2

def pole_prostokątu(z,c):
    return z*c

def pole_trójąta(a,h):
    return (a*h)/2

def pole_sześcianu(m):
    return ((m**2)*6)

while True:
    print("Dostępne opcje: ")
    print("Opcja a: pole koła")
    print("Opcja b: pole kwadratu")
    print("Opcja c: pole prostokątu")
    print("Opcja d: pole trójkąta(z wysokością)")
    print("Opcja e: pole sześcianu")
    print("Wybór: ")
    inp = input()
    if inp == 'stop':
        break
    elif inp == 'a':
        print("podaj zmienną")
        r = float(input())
        print(pole_koła(r))
    elif inp == 'b':
        print("podaj zmienną")
        y = float(input())
        print(pole_kwadratu(y))
    elif inp == 'c':
        print("podaj zmienną")
        z = float(input())
        print("podaj 2 zmienną")
        c = float(input())
        print(pole_prostokątu(z,c))
    elif inp =='d':
        print("podaj zmienną")
        a = float(input())
        print("podaj 2 zmienną")
        h = float(input())
        print(pole_trójąta(a,h))
    elif inp == 'e':
        print("podaj zmienną")
        m = float(input())
        print(pole_sześcianu(m))
    
    else:
        print("nie ma takiej komendy")

    print("")    
    input("Naciśnij Enter aby kontynuować ...")
    print("")
