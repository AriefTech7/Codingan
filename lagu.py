from time import sleep
import sys

def print_lirik():
    lines = [
        ("Merah pipi kamu" 0.10),
        ("Aku lihat kamu senyum padaku", 0.10),
        ("Ku tahu kamu suka padaku", 0.10),
        ("Tapi kamu ragu bilang begitu", 0.10),
        ("Terlalu lama kamu membuang waktumu", 0.22),
        ("Gak pake lama", 0.15),
        ("Bilang saja kalau kau suka", 0.16),
        ("Gak pake lama", 0.15),
        ("Bilang saja kalau kau suka", 0.16),
        ("Dan aku juga suka", 0.17),
        ("Suka kamu", 0.14),
        ("Ku tunggu sampai kamu bilang I love you", 0.17)
    ]

    for line, char_delay in lines:
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)
        print()

print_lirik()