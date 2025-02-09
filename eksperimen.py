


def program():
    data_siswa = {
    'nama':'nama',
    'sim':00000,
    'kelas':0,
    'jurusan':'jurusan'
}
    tambahan_data ={}
    while True:
        print(f"{'SELAMAT DATANG':^20}")
        print(f"{'DATA SISWA LABOR':^20}")
        print("-"*20)

        data =  dict.fromkeys(data_siswa)
        data['nama'] = input("masukkan nama siswa/siswi\t:")
        data['sim'] = int(input("masukkan sim siswa/siswi\t:"))
        data['kelas'] = int(input("masukkan kelas siswa/siswi\t:"))
        data['jurusan'] = input("masukkan jurusan siswa/siswi\t:")
        print("_"*70)
        print(data)

        tambahan_data.update({'key':data})
    
        print('_'*70)

        for siswa in tambahan_data:
            KEY = siswa

        NAME = tambahan_data[KEY]['nama']
        SIM = tambahan_data[KEY]['sim']
        KELAS = tambahan_data[KEY]['kelas']
        JURUSAN = tambahan_data[KEY]['jurusan']

        print(f"{KEY:<6} {SIM:<17} {KELAS:<3} {JURUSAN:^9}")

        print("\n")
        done = input("sudah atau belum bro yes/no\t:")

        if done == 'no':
            print("selamat tinggal")
            break

program()