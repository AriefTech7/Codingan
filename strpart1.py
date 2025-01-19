print("=========operasi dan manipulasi string part 1=============")
#1.mengabungkan string (concatenation)
nama_pertama ="ucup"
nama_kedua ="D"
nama_ketiga = "Farame"

nama_lengkap =nama_pertama + " " + nama_kedua + "'" + nama_ketiga
print("nama panjang ucup : " + str(nama_lengkap))

#menghitung panjang string
p = len(nama_lengkap)
print(p)



# mengecek apaakah ada komponen char atau string di string
d = "f"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

#mengulang string
halo = ("halo semuanya ")
print(halo*2)

#indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1])# dari belakang 
print("index ke-(-3) : " + nama_lengkap[-3])# dari belakang 
print("index ke-[0:4] : " + nama_lengkap[0:4])
print("index ke-[4:13] : " + nama_lengkap[4:13])# : artinya sampai
print("index ke-[4:12] : " + nama_lengkap[4:12])# : artinya sampai
print("index ke-[4:11] : " + nama_lengkap[4:11])# : artinya sampai

print("index ke-[0,1,2,3,4,5,6,8,10] : " + nama_lengkap[0:11:2])# : artinya sampai
""""
1.nama_lengkap[0:11:2]

Ini adalah slice atau pemotongan string dengan format:
[start:end:step], yang berarti:
start: Mulai dari indeks 0.
end: Berhenti di indeks 11 (tidak termasuk indeks 11).
step: Ambil setiap 2 karakter.
2.nama_lengkap String:

Isi string nama_lengkap adalah:
"ucup D'Farame"

Indeksnya:

u  c  u  p     D  '  F  a  r  a  m  e
0  1  2  3  4  5  6  7  8  9 10 11 12
3.Hasil nama_lengkap[0:11:2]

Karakter yang diambil adalah dari indeks 0 sampai 10 (karena end=11 tidak termasuk).
Dengan step=2, kita mengambil setiap 2 indeks:
Indeks ke-0: 'u'
Indeks ke-2: 'u'
Indeks ke-4: ' '
Indeks ke-6: '\'' (karakter ')
Indeks ke-8: 'r'
Indeks ke-10: 'a'
"""
#nilai paling kecil
print("paling kecil: " + min(nama_lengkap))#Mengembalikan karakter alfabetik dari string str.
#nilai paling besar
print("paling besar: " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 177
print("ASCII code untuk 177 adalah " + chr(data))

#operator bentuk method

data = "otong kemana otong"
jumlah = data.count("a")
print(f"jumlah huruf A dari {data} adalah " + str(jumlah))

print("=========string width(lebar) & alignment(penyelarasan)=============")

# width

#ljust rjust center
text = "ITB"
print(text.ljust(15,"="))
print(text.rjust(15,"+"))
print(text.center(15,"-"))

#fstring 
# sintaks {variable:><^width}
print(f"{text:>15}")
print(f"{text:<15}") 
print(f"{text:^15}")

nama = "kuncup"
kelas = "12"
sekolah = "smk labor"
print(f"""
nama    = {nama}
kelas   = {kelas}
sekolah = {sekolah}
""")


tabel = ["nama", "NIS", "jurusan"]
nama = ["timo", "222100", "TKJ"]
print(f"{tabel[0]:<10} | {tabel[1]:^10} | {tabel[2]:>10}")
print("="*37)
print(f"{nama[0]:<10} | {nama[1]:^10} | {tabel[2]:>10}")