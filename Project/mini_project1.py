#Program untuk menghitung gaji bulanan seseorang berdasarkan jam kerja dan gaji per jam.

nama = input("masukan nama anda: ") #str
jam_kerja = int(input("masukan total jam kerja dalam per bulan:")) # int
tarif_per_jam = float(input("masukan gaji per jam:")) # float

#hitung total gaji
total_gaji =  jam_kerja * tarif_per_jam

#tampilkan hasil
print(F"nama : {nama}")
print(f"total jam kerja : {jam_kerja}jam ")
print(F"gaji per jam : Rp{tarif_per_jam} ")
print(F"total gaji bulanan : Rp{total_gaji}")
