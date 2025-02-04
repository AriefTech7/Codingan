# LIST
#teman = ["timo", "jaiz", "darwin"]
#teman_dekat = ["timo", "farras" ,"fikri"]
#teman.extend(teman_dekat)
#teman.append("aziz")
#teman.insert(0, "udin") # teman.insert(posisi, data yang mau dimasukkan)
#del teman[0]
#print(teman)
#print(teman[0])
#print(f"data index pertama {teman[2]}")

#utang = ["rizal", "abdul", "starboy"]
#uang = [5000, 10000, 20000]
#utang.extend(uang)
#print(utang)
#print (uang)

#data_range = list(range(0, 10))
#print(data_range)

## list comprehensions

#nomor = [x for x in range(10) if x % 2 == 0]
#print(nomor)
## menggunakan ekspresi dalam list comprehensions

#hitung = [x**2 for x in range(11)]
#print(hitung)

#numbers = [4, 5,6, 7, 4, 2, 8, 12, 12, 4, 10 ,13]

#print(f"jumlah angka  =  {numbers.count(2)}")

##mengurutkan list
#numbers.sort()
#print(f"mengurutkan data = \n{numbers}")


## membalikan list
#numbers.reverse()
#utang.reverse()
#print(f"data reverse= \n{numbers} \n {utang}")

## menduplikat list / copt list
data = [11, "kamu", 33, "saya", 55, "madu", 77]
data1 = [11, "kamu", 33, "saya", 55, "madu", 77]

data[1] = "wahyu"
data2 = data.copy()

print(data1)
print(data2)
print(data)





def main():
    data = [11, 22, 33, 44, 55]
    
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    print(data[4])
    print(data[-1])


#main()


def main():
    data = [11, "kamu", 33, "saya", 55]
    
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    print(data[4])
    print(data[-1])


#main()


## nested list / list didalam list

li = [1, "santi", ["Jl.bunga 12", "bandung", 20111], "20-12-2012"]
print(li)

data_0 = [11, 22]
data_2 = [33, 55, 66]
print(data_0, data_2)

# contoh penggunaannya
 
peserta0 = ["udin", 17, "panam"]
peserta1 = ["nando", 18, "rumbai"]
peserta2 = ["nanda", 17, "rumbai"]

li_peserta = [peserta0, peserta1, peserta2]
print(li_peserta)

for peserta in li_peserta:
    print(f"nama \t= {peserta[0]}")
    print(f"umur \t= {peserta[1]}")
    print(f"tempat tinggal \t= {peserta[2]}\n")


data_nama = ["bandrul", "anton"]
data_nama2 = ["lim", "ahmad"]

data_gabung = [data_nama, data_nama2, 10]

# mengambil data nested list
data_gabung_copy = data_gabung.copy()
print(data_gabung[0][0]) # maksudnya ia mangambil data dilist data_gabung pada data 0 dan didalam data 0 ia mengambil data 0

# addresss 
print(f"address asli = {hex(id(data_gabung))}")
print(f"address asli = {hex(id(data_gabung_copy))}")

data_gabung[1][0] ="upin"


print(f" data = {data_gabung}")

# deepcopy list

from copy import deepcopy
data_gabung = [data_nama, data_nama2, 10]
data_deepcopy = deepcopy(data_gabung)

print(f"address asli = {hex(id(data_gabung))}")
print(f"address asli = {hex(id(data_deepcopy))}")


## looping list dan enumerate

# for loop 

li = [1,3,46,7,12,446,78,]

for angka in li:
    print(f"ini = {[angka]}")


tkj = ["daffa", "yuda", "ricard", "aziz", "latifa", "dea", "bita", "messi", "sokep"]

for nama in tkj: # nama berfungsi untuk menyimpan setiap elemen dalam list tersebut
    print(f"berikut adalah nama anak 12 tkj = {nama}")

# enumerate

for index, teman in enumerate(tkj): # enumerate berfungsi untuk menampilkan pada posisi/indeks mana elemen tersebut berada
    print(f"index = {index}, nama teman = {teman}")# index hanya variabel, sekali lagi ingat index itu hanya variabel dan bisa diganti seperti contoh berikut

for posisi, teman in enumerate(tkj):
    print(f"index = {posisi}, nama teman = {teman}")

for posisi, teman in enumerate(tkj, start=1):# kta juga bisa mengubah start enumerate yang secara default dimulai dari 0. kita menggantinya menggunakan start=(nomor) 
    print(f"index = {posisi}, nama teman = {teman}")

i = 0
while i < len(tkj):
    print(tkj[i])
    i +=1 # i +=1 == i + 1  

print("===Latihan===")

buah = ['apel', 'mangga', 'pisang', 'jeruk', 'anggur']

#for nomor, nama_buah in enumerate(buah, start=1):
#    print(f"buah ke-{nomor}: {nama_buah}")

for angka, makan in enumerate(buah, start=10):
    print(f"indeks : {angka}, buah : {makan}")


angka = [12, 3, 7, 25, 10, 8, 15]

for index, nomor in enumerate(angka):
    if nomor > 10:
            print(f"angka yang lebih besar dari 10: \n index = {index} & angka = {nomor}")


a = 0
print(f"panjang list 5")
while a < len(buah):
     print(buah[a])
     a += 1


angka = [1, 2, 3, 4, 5]

for nmr in enumerate(angka):
     print(angka)

input("masukan nama buah-1 :")
input("masukan nama buah-2 :")
input("masukan nama buah-3 :")
input("masukan nama buah-4 :")
input("masukan nama buah-5 :")


print("Hasil:")
for angka, buah in enumerate (input):
     print(f"index : {angka}, nama : {buah}")


## program list buku sederhana

list_buku = []

while True:
     judul = input("masukkan judul buku\t:")
     penulis = input("masukkan nama penulis\t:")

     buku = [judul, penulis]
     list_buku.append(buku)

     for index, buku in enumerate(list_buku, start=1):
          print(f"{index} | {buku[0]} | {buku[1]}")

     lanjut = input("Apakah lanjut (y/n)")

     if lanjut == "n":
          break
print("PROGRAM SELESAI")


# latihan

buah = []

for a in range(5):
     nama = input(f"masukan nama buah ke-{a+1}\t:")
     buah.append(nama)

print("Hasil:")
for ind, nama in enumerate(buah):
     print(f"index = {ind}, buah = {nama}")


kata = ['saya', 'sedang', 'belajar', 'python']

for inx, kt in enumerate(kata):
     print(f"kata = {kt}, Jumlah karakter = {len(kt)}")

matrix = [
     [1,2,3],
     [4,5,6],
     [7,8,9]
]

for d, nmr in enumerate(matrix):
     print(f"baris ke-{d}: {nmr}")

for brs in matrix:
    for elemen in brs:
          print(elemen, end=" ")# end ="" -> berfungsi untuk mengatur apa yang akan dioutput
    print()