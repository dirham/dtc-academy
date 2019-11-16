panjang_segitiga = input("Masukkan panjang segitiga : ")



for i in range(0, int(panjang_segitiga)):
    for j in range(0, i + 1):
        print("* ", end="")
    print('')


print('=======================while===================')
loopke_1 = 0
while loopke_1 <= int(panjang_segitiga):
    j = loopke_1
    # print(j)
    while j > 0:
        print("* ", end="")
        j = j - 1
    loopke_1 = loopke_1 + 1
    print("")

print('=======================putar===================')
loopke_1 = 0
while loopke_1 <= int(panjang_segitiga):
    j = loopke_1
    # print(j)
    while j < int(panjang_segitiga):
        print("* ", end="")
        j = j + 1
    loopke_1 = loopke_1 + 1
    print("")