# buat variable list
my_list = ["golang", "PHP", "Python"]
# keluarkan isi my_list secara manual
print(my_list[0])

# buat variable tupel
my_tupel = ("Nasi Kuning", "es teh", "Nasi Putih")
# keluarkan nilai / isi my_tupel secara manual
print(my_tupel[len(my_tupel)-1])

# buta dictonary
my_dict = {"nama": "Sarah", "alamat": "Makassar", "umur": 20, 8:"coba-coba", "isi_tupel": my_tupel, "isi_list": my_list}
# keluarkan nilai / isi my_dict secara manual
print(my_dict["isi_tupel"][1]+ " " +my_dict["isi_tupel"][0])
print(my_dict["isi_list"][0])