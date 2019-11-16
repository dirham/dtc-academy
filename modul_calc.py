def say_halo(nama = "World"):
    print("Haloo "+nama)

def simple_calc(nilai_a = 0, nilai_b = 0, operator=""):
    if operator == "+":
        return nilai_a + nilai_b
    elif operator == "-":
        return nilai_a - nilai_b
    elif operator == "/":
        return nilai_a / nilai_b
    else:
        return "masukkan operator"

def printFibb(nilai):
    i = 0
    n1 = 0
    n2 = 1
    while i <= nilai :
        if i == 0:
            print(0)
            i = i + 1
        elif i == 1:
            print(1)
            i = i + 1
        else:    
            nth = n1 + n2
            print(nth)
            n1 = n2
            n2 = nth
            i = i + 1