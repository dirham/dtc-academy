def cal_me(life):
    if life < 1:
        print(life)
        return 0
    print("masih ada nyawa "+ str(life))
    return cal_me(life - 1) 

hasil = cal_me(6)

print(hasil)