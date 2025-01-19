print("=========logikabool=============")

#OR(jika salah satu true, maka hasilnya true)#
##x = True
##y = False
#print(y or y)
#print(x or y)
#print(y or x)
#AND(jika salah satu false, maka hasilnya false)#
#print(x and y)
#print(y and x)
#print(x and x)


#NOT(jka nilai true, maka hasilnya false dan begitu sebaliknya)
#print(not x)
#print(not y)

#umur = 17
#income = 5000000

#if umur > 10 and income < 5000000:
#    print("persyaratan terpenuhi")
#else:
#    print("persyaratan tidak terpenuhi")


#if umur < 18 or income > 4000000:
#    print("salah satu syarat terpenuhi")
#else:
#    print("salah satu syarat tidak terpenuhi")#

    
#a = True
#b = False
#c = True
#z = False
#hasil = a or b and z
#print(hasil)

#XOR(akan true jika salah satu true, sisa false)
###a = True
###b = False
###c = True
###d = False
###hasil1 = a ^ b
###hasil2 = b ^ a
###hasil3 = a ^ c
###hasil4 = b ^ d
###print(hasil1)
###print(hasil2)
###print(hasil3)
###print(hasil4)




#username = input("masukan username:")
#password = int(input("masukkan password:"))

#if username == "admin" or password == "098":
#    print("Login berhasil!")
#else:
#    print("Login gagal.")


#role = input("masukan role kamu:")
#status_active = True

#if role == "admin" and status_active:
#    print("Akses penuh diberikan.")
#elif role == "user" and status_active:
#    print("Akses terbatas diberikan.")
#else:
#    print("Akses ditolak.")

#\n = enter \t = spasi ditulis pada codingan

print("====Latihan Komparasi dan Logika====")

#membuat gabungan area rentang dari angka

#inputangka = float(input("masukkan angka yang \nkurang dari 3 \natau \nlebih dari 10:")) 

#if inputangka <= 3:
#    hasil = (inputangka <= 3)
#    print("kurang dari 3 :", hasil)
#elif inputangka >= 10:
#    hasil2 = (inputangka >= 10)
#    print("lebih dari 10 :", hasil2)
#else:
#    print(inputangka < 3)
    
#angka = float(input("masukkan angka yang \nkurang dari 3 \natau \nlebih dari 10:")) 

#+++3----------------
#kurang = (angka < 3)
#print("kurang dari 3 :", kurang)

#------------------10++++++++
#lebih = (angka> 10)
#print("lebih dari 10:", lebih)

#benar = kurang or lebih
#print("angka yang dimasukkan :", benar)

#-----0+++++5------8++++++11------
ang = float(input("masukan angka \nlebih dari 0 \nkurang dari 5 \nlebih dari 8 \nkurang dari 11: "))

operasi1 =(ang  > 0 )
print("lebih dari 0:", operasi1)

operasi2 = (ang < 5)
print("kurang dari 5:", operasi2)

operasi3 = (ang > 8)
print("lebih dari 8:", operasi3)

operasi4 = (ang < 11)
print("kurang dari 11:", operasi4)
#+++++0-----5++++++8------11++++++

angka = float(input("masukan angka \nkurang dari 0 \nlebih dari 5 \nkurang dari 8 \nlebih dari 11: "))

op1 =(angka < 0)
print("kurang dari 0:", op1)

op1 =(angka > 5)
print("lebih dari 5:", op1)

op1 =(angka < 8)
print("kurang dari 8:", op1)

op1 =(angka > 11)
print("lebih dari 11:", op1)