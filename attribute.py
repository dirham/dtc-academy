class Motor:
    def __init__(self):
        print ("Di statar")
        self.nama = "Jirayya"
        self.__pembuat = "Kappa"
        self._keluaran = 2019
    def nge_gas(self,type_kenalpot):
        if type_kenalpot == "bogar":
            print("brooombbbbbbbbooooomm.. brooombbbbbbbbooooomm.. brooombbbbbbbbooooomm." )
        else:
            print("ngeengggg... ngeenngg.. ngeenngg...")
    
    def cal_pembuat(self):
        print(self.__pembuat)


    def set_pembuat(self, nama):
        self.__pembuat = nama
        # return self.__pembuat
    # panggil class
motor_ari = Motor()

print(motor_ari.nama)
motor_ari.nge_gas("bogar")
motor_ari._keluaran = "mm"
print(motor_ari._keluaran) # protected atribute masih bisa di panggil atau di ubah.
print(motor_ari.__pembuat) # hilangkan komentar dan coba jalankan
# motor_ari.set_pembuat("Honda")
motor_ari.cal_pembuat()