# Membuat List
list_bahasa_pemrograman = ("Python", "Ruby", "PHP", "JAVA", "Javascript", "Golang", "C", "C++", "C#")
# defenisikan variable i = 0
i = 0
# perulangan "loop" dengan while untuk menampilkan datanya
while i < len(list_bahasa_pemrograman):
    print(list_bahasa_pemrograman[i])
    # menambahkan nilai satu pada variable i setiap kali perulangan
    i = i+1

print("==================================================================================")

print("menampilkan data pada variable \"list_bahasa_pemrograman\" dengan for loop")
print("==================================================================================")
for bhs_pemrograman in list_bahasa_pemrograman:
    print(bhs_pemrograman)
