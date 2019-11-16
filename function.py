def cal_me(param):
    nilai = param + 1
    return cal_me(nilai)

hasil = cal_me(1)

print(hasil)