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

user = input("give me your user: ")
if user == "admin":
    print("user accepted")
    print("welcome to the hell of university")
elif user == "andi":
    print("user accepted")
    print(f"welcome to world {user}")
elif user == "arif":
    print("user accepted")
    print(f"welcome to home {user}")
else:
    print("user not accepted")



