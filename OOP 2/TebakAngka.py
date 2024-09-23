""" 
    created:18 January 2024
    desc:Program tebak angka
    author: Mundung, Brainer Keneth
"""
""" 
    created:18 January 2024
    desc:Program tebak angka
    author: Mundung, Brainer Keneth
"""

#import random
import random

#range angka 
n = random.randrange(1, 10)
kesempatan = 5

def guessing():
#tempat memasukan angka yang akan ditebak
    tebak = int(input("Masukan angka: "))

#Loop
    while n!= tebak:
        if tebak < n:
            print("Angka yang di tebak telalu kecil")
            tebak = int(input("Silahkan input lagi: "))
        elif tebak > n:
            print("Angka yang ditebak terlalu besar")
            tebak = int(input("Silahkan input lagi: "))
        break

    print("Selamat tebakan anda benar!!!")  
guessing()