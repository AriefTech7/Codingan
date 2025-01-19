# LIST
teman = ["timo", "jaiz", "darwin"]
teman.append("aziz")
teman.insert(0, "udin") # teman.insert(posisi, data yang mau dimasukkan)
#del teman[0]
print(teman)
#print(teman[0])
#print(f"data index pertama {teman[2]}")

#tuple
#bulan = ("januari", "february", "mei", "juni", "juli", "november", "september")
#print(bulan[6])
#print(bulan[3])

#set
#nomor = {1, 2, 3, 4, 5}
#nomor.add(6)
#nomor.add(7)
#nomor.remove(4)
#nomor.add(7)
#print(nomor)

#dictionary
#siswa={"nama": "timo", "usia":"17", "kelas":"12TKJ"}
#siswa["nilai ujian"] = "89"
#siswa["usia"] = "19"
#print("semua key:", siswa)

#mini project
#list_belanja = ["sabun", "shampoo", "sikat gigi", "odol", "rinso", "snack"]
#list_belanja.append ("pocari")
#del list_belanja[3]
#print("semua list belanja:", list_belanja)


nilai = 84

if nilai >= 80 and nilai <= 90:
    print("niali A")
elif nilai >= 85:
    print("nilai B")
else:
    print("nilai C")


utang = ["rizal", "abdul", "starboy"]
uang = [5000, 10000, 20000]
print(utang)
print (uang)

data_range = list(range(0, 10))
print(data_range)

## list comprehensions

nomor = [x for x in range(10) if x % 2 == 0]
print(nomor)
## menggunakan ekspresi dalam list comprehensions

hitung = [x**2 for x in range(11)]
print(hitung)



