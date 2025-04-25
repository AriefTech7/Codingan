# latihan perulangan membuat segitiga

sisi = 10

count = 1
for i in range(sisi):# for loop
    print("*"*count)
    count +=1




count = 1
while True:
    if (count%2):
        print("*"*count)
        count +=1

    else:
        count +=1
        continue

    
    
    if count > sisi :
        break



print("awal For")
count = 1
for i in range(sisi):
	print("*"*count)
	count += 1

print("akhir dari for")
# 2. Menggunakan while

print("awal while")
count = 1
while True:
	print("*"*count)
	count += 1

	if count > sisi:
		break

print("akhier while")


print("awal while") # hanya ganjil saja
count = 1

while True:
        if (count%2):
            print("*"*count)
            count += 1

        else:
            count += 1
            continue

        if count > sisi:
             break
        
print("akhir while")

print("awal while")
count = 1
spasi = int(sisi/2)

while True:
        if (count%2):
          print(" "*spasi,"+" *count)
          spasi -= 1
          count += 1

        else:
             count += 1
             continue
        
        if count > sisi:
             break
        
print("akhir while")

print("awal while")
sisi = int(input("Masukkan panjang sisi ketupat (harus angka ganjil): "))

# Validasi input agar ganjil
if sisi % 2 == 0:
    print("Panjang sisi harus angka ganjil!")
    exit()

# Bagian atas ketupat
count = 1
spasi = sisi // 2

while count <= sisi:
    if count % 2:  # Hanya mencetak jika count ganjil
        print(" " * spasi + "+" * count)
        spasi -= 1
    count += 1

# Bagian bawah ketupat
count = sisi - 2
spasi = 1

while count > 0:
    if count % 2:  # Hanya mencetak jika count ganjil
        print(" " * spasi + "+" * count)
        spasi += 1
    count -= 1

print("akhier while")

     
    

