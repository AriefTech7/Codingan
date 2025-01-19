import datetime  as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"hari ini adalah = {hari_ini:%A}")# %A -> untuk hari
hari_ini = dt.date(2007,1,29)
print(hari_ini)
print(f"hari ini adalah = {hari_ini:%A}")# %A -> untuk hari



print("Silahkan masukkan tanggal, bulan dan tahun kelahiran : ")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tangga lahir adalah {tanggal_lahir} dan hari adalah {tanggal_lahir:%A}")


hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah = {hari_ini:%A}")# %A -> untuk hari
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"sekarang pada {hari_ini} berumur : {umur_tahun}")