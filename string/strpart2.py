print("=========operasi dan manipulasi string part 2=============")

# merubah case dari string
salam = "bro!"
print("normal =" + salam)

# upper -> merubah semua ke upper case

print("upper = " + salam.upper())

# capitalize -> meng-kapitalkan huruf pertama string
print("capital : " + salam.capitalize())
# swapcase -> Menukar huruf besar menjadi kecil dan sebaliknya
print(salam.swapcase())

#replace ->Mengganti bagian string dengan teks lain
z = "halo dunia" 
#z.replace("old", "new")
print(f"{z} ini replace: " + z.replace("halo", "hai"))




ucap = "aKyu lOve tO yoU"
# lower : Mengonversi semua huruf besar dalam bentuk string menjadi huruf kecil.
print("lower : " +  ucap.lower())
# strip : Menghapus spasi di awal dan akhir string.
teks = " welcome "
print("menghapus spasi awal dan akhir : " + teks.strip())
# count : menghitung berapa kata
buah = "semangka, apel, manggis"
print("count : " + str(buah.count("a")))
# pengecekan lower case (islower)
kata = "kamyu"
print(f"{kata} is lower : " + str(kata.islower()))
# pengecekan upper case (isupper)
kata1 = "KAmYU"
print(f"{kata1} is upper : " + str(kata1.isupper()))

# isalpha() -> untuk mengecek semua huruf
print(f"{kata1} is alpha : " + str(kata1.isalpha()))
# isalnum() -> memeriksa apakah string hanya berisi angka dan huruf
print(f"{kata1} is alnum : " + str(kata1.isalnum()))
# isdigit() -> memeriksa apakah string hanya angka
print(f"{kata1} is digit : " + str(kata1.isdigit()))
# isspace() -> spasi, tab, newline \n
print(f"{kata1} is space : " + str(kata1.isspace()))

# istittle() -> semua kata dimulai dengan huruf besar
kata2= "Zona Merah"
print(f"{kata2} is tittle : " + str(kata2.istitle()))
kata3= "Zona merah"
print(f"{kata3} is tittle : " + str(kata3.istitle()))

## mengecek komponen startswith() -> memeriksa str diawal dengan kalimat tertentu
paragraf = "Pagi itu, hujan baru saja reda. Cahaya matahari menerobos awan dan memantul di genangan air di depan rumah. Di jendela kamarnya, seorang anak bernama Lia memperhatikan seekor kupu-kupu yang hinggap di kaca. Sayapnya yang berwarna-warni tampak basah dan lemah."
print(f"{paragraf} is startswitch: " + str(paragraf.startswith("Pagi itu, hujan baru saja reda")))
## mengecek komponen  endswith() -> memeriksa str diakhir dengan kalimat tertentu
print(f"{paragraf} is endswitch: " + str(paragraf.endswith("Sayapnya yang berwarna-warni tampak basah dan lemah.")))
## penggabungan komponen join() -> menggabungkan teks dari beberapa bagian menjadi satu dengan tipe data list
kalimat = ["saya", "suka", "Python"]
print(f"{kalimat} is join: " + " ".join(kalimat))
print(f"{kalimat} is join: " + "-".join(kalimat))
## penggabungan komponen  split() -> memisahkan teks menjadi beberapa bagian kecil.
kalimat1 = " saya suka python"
print(f"{kalimat1} is split: " + str(kalimat1.split()))
## alokasi karakter rjust() ljust() center()
tengah = "hai".center(20,"-")
print("'"+tengah+"'")
 
kanan = "helo".rjust(20)
print("'"+kanan+"'")

kiri = "hai".ljust(20)
print("'"+kiri+"'")

tengah = tengah.strip("-")
print(tengah)

#Slicing: Mengambil beberapa karakter dari string.
teks = "welcome to real world"
print(teks[:7])

#Indexing: Mengambil karakter pada posisi tertentu.
print(teks[9])

#find(): Mencari posisi pertama teks tertentu
cerita = "Lia membuka jendela perlahan agar tidak mengagetkan kupu-kupu itu. Ia meletakkan jarinya di dekatnya, dan kupu-kupu tersebut merangkak naik. Lia tersenyum kecil. ""Kamu pasti kehujanan, ya"" gumamnya."
print(f"{cerita} is find : " + str(cerita.find("membuka")))

#index(): Sama seperti find(), tetapi akan menghasilkan error jika teks tidak ditemukan.
print(f"{cerita} is find : " + str(cerita.index("halo")))

