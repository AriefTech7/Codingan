# LIST
teman = ["timo", "jaiz", "darwin"]
teman_dekat = ["timo", "farras" ,"fikri"]
teman.extend(teman_dekat)
teman.append("aziz")
teman.insert(0, "udin") # teman.insert(posisi, data yang mau dimasukkan)
#del teman[0]
print(teman)
#print(teman[0])
#print(f"data index pertama {teman[2]}")

utang = ["rizal", "abdul", "starboy"]
uang = [5000, 10000, 20000]
#utang.extend(uang)
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

numbers = [4, 5,6, 7, 4, 2, 8, 12, 12, 4, 10 ,13]

print(f"jumlah angka  =  {numbers.count(2)}")

##mengurutkan list
numbers.sort()
print(f"mengurutkan data = \n{numbers}")


##membalikan list
numbers.reverse()
utang.reverse()
print(f"data reverse= \n{numbers} \n {utang}")

## menduplikat list

