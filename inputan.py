umur = input("masukkan umur : ")

umur_int = int(umur)

if umur_int <= 17:
    print("di bawah umur")
elif umur_int >= 20 and umur_int <=30:
    print("Jomblo masih di toleransi!")
elif umur_int > 35 and umur_int <= 37:
    print("lampu kuning")
else:
    print("perbanyak berdoa dan sedekah")

print(umur_int is not 20)