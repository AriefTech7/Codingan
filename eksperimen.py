# import google.generativeai as genai
# import numpy as np
# import matplotlib.pyplot as plt

# # Masukan Api Key gemini
# genai.configure(api_key="API_KEY")

# # Inisialisasi papan Tic-Tac-Toe
# board = np.full(9, " ")

# # Posisi koordinat grid untuk menggambar Tic-Tac-Toe
# positions = [(x, y) for y in range(2, -1, -1) for x in range(3)]

# # Fungsi menggambar papan
# def draw_board():
#     plt.clf()
#     plt.xlim(-0.5, 2.5)
#     plt.ylim(-0.5, 2.5)
#     plt.xticks([])
#     plt.yticks([])

#     # Garis Grid
#     for i in range(1, 3):
#         plt.plot([i-0.5, i-0.5], [-0.5, 2.5], color='black', lw=3)
#         plt.plot([-0.5, 2.5], [i-0.5, i-0.5], color='black', lw=3)

#     # Gambar X dan O
#     for i, pos in enumerate(positions):
#         if board[i] != " ":
#             plt.text(pos[0], pos[1], board[i], fontsize=40, ha='center', va='center',
#                      color='red' if board[i] == 'X' else 'blue')

#     plt.title("Klik pada papan untuk memilih langkah!")
#     plt.draw()

# # Fungsi mengecek kemenangan
# def check_winner():
#     win_states = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
#                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
#                   (0, 4, 8), (2, 4, 6)]
    
#     for a, b, c in win_states:
#         if board[a] == board[b] == board[c] and board[a] != " ":
#             return board[a]
    
#     return "Draw" if " " not in board else None

# # Fungsi meminta langkah Gemini
# def get_gemini_move():
#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         prompt = f"""
#     Kamu adalah AI yang bermain Tic-Tac-Toe. Berikut papan saat ini:
    
#     {board[0]} | {board[1]} | {board[2]}
#     {board[3]} | {board[4]} | {board[5]}
#     {board[6]} | {board[7]} | {board[8]}
    
#     Pilih langkah terbaik dengan angka (0-8) sesuai posisi kosong.
#     """
    
#     response = model.generate_content(prompt)
#     try:
#         move = int(response.text.strip())
#         if move in range(9) and board[move] == " ":
#             return move
#     except Exception as e:
#         print(f"Error accessing Gemini API: {str(e)}")
    
#     return np.random.choice(np.where(board == " ")[0])

# # Fungsi menangani klik pengguna
# def on_click(event):
#     global board

#     if event.xdata is None or event.ydata is None:
#         return  

#     x, y = int(round(event.xdata)), int(round(event.ydata))
#     if (x, y) in positions:
#         index = positions.index((x, y))
#     else:
#         return

#     # Jika kotak kosong, letakkan X
#     if board[index] == " ":
#         board[index] = "X"
#         draw_board()

#         # Cek apakah pemain menang
#         if (winner := check_winner()):
#             print(f"Pemenang: {winner} 🎉")
#             plt.title(f"Pemenang: {winner} 🎉")
#             plt.draw()
#             return

#         # Giliran Gemini
#         print("Giliran Gemini...")
#         board[get_gemini_move()] = 'O'
#         draw_board()
# ... (15 lines left)
# username = input("masukan username anda:\n")
# if username == "admin":
#     print("username diterima")
# else:
#     print("username tidak diterima")

# print(f"selamat datang di aplikasi ini {username}")

# user = input("give me your user: ")
# if user == "admin":
#     print("user accepted")
#     print("welcome to the hell of university")
# elif user == "andi":
#     print("user accepted")
#     print(f"welcome to world {user}")
# elif user == "arif":
#     print("user accepted")
#     print(f"welcome to home {user}")
# else:
#     print("user not accepted")


def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    kelas = data[1]
    umur = data[2]

    print(f"{nama} adalah siswa dikelas {kelas} dan baru menginjak umur {umur}")

fungsi(["andi",12,19])


def data(*args):
    nama = args[0]
    kelas = args[1]
    umur = args[2]

    print(f"{nama} adalah siswa dikelas {kelas} dan baru menginjak umur {umur}")

data("udin",11,18)


def proses(*data):
    nama = data[0]
    sekolah = data[1]
    status = data[2]
    kelas = data[3]

    print(f"{nama} adalah siswa biasa yang bersekolah di smk {sekolah} dan sudah menginjak {kelas} dari smp ia masih berstatus {status}")

proses("wahyu","labor","single",12)


def contoh_fungsi(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

contoh_fungsi(nama="John", umur=25, kota="Jakarta")


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



