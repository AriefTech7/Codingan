print("=========cantinue, pass & break=============")
# continue & pass & break
print("=========pass=============")

# pass -> dia berfungsi sebagai dumy, tidak akan dieksekusi


#def sapa():
#    print("hallooo")
#    pass# pass berfungsi untuk tidak menjalankan code function 

#print(sapa)

for i in range(5):
    if i == 2:
        pass  # Tidak melakukan apa-apa ketika i adalah 2
    print(i)


# continue
print("=========continue=============")
#angka = 0

#print(f"angka sekarang -> {angka}")

#while angka < 5:
#	angka += 1
#	print(f"angka sekarang -> {angka}") # aksi 1

#	if angka == 3:
#		print("nice!")
#		continue # akan membuat loop meloncat ke step selanjutnya

#	print("whassup!") # aksi 2

#print("Pinish!")

angka = [1, 2, 3, 4, 5]

for num in angka:
    if num == 3:
        continue  # Lewati angka 3
    print(num)

	
	


# Break
print("=========break=============")

for angka in range(10):  # Loop dari 0 sampai 9
    print(f"Memeriksa angka: {angka}")
    if angka == 5:       # Jika angka adalah 5
        print("Angka 5 ditemukan, menghentikan loop.")
        break            # Loop berhenti
print("Selesai.")


i = 0
while i < 10:
    print(f"Memeriksa angka: {i}")
    if i == 7:           # Jika angka adalah 7
        print("Angka 7 ditemukan, menghentikan loop.")
        break            # Loop berhenti
    i += 1
print("Selesai.")






