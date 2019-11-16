def say_hello():
    print("Hello " + nama)

nama = input("Masukkan nama anda : ")
say_hello()

# function dengan default data

def say_hello_default(nama = "World"):
    print("Hello " + nama)

say_hello_default()

# task buat function yang di dalamnya ada if else jika tidak ada data nama di masukkan maka tampilkan world
def say_hello_v2(nama):
    if nama == "":
        nama = "World"
        print("Hello " + nama)
    else:
        print("Hello " + nama)

nama_v2 = input("Masukkan nama anda pada function 2: ")
say_hello_v2(nama_v2)