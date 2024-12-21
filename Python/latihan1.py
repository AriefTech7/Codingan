umur = "16"
s = int(umur)
print(s)

siswa = "arif, yuda, charlie"
print(siswa)

# tipe data koleksi list

buah = ["apel", "semangka", "anggur", "jeruk"]
print(buah)
buah[2] = "mangga"
print(buah)

buah.append ("berry")
print(buah)

# tipe data koleksi tuple

warna = ("merah", "kuning", "hijau")
print(warna)
print(warna[1])

# tipe data koleksi set

hari = {"senin", "selasa", "rabu", "kamis", "jumat", "sabtu"}
hari.add("minggu")
hari.remove("sabtu")
print(hari)

# tipe data koleksi dictionary
orang = {"nama" : "wahyu", "umur" : "19", "kota" : "PKU"}
orang["pekerjaan"] = "devops"
del orang ["kota"]
print(orang["nama"])
print(orang)