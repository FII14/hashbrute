#!/usr/bin/env python

import hashlib
import os
import sys
import time
import threading

# Algoritma hash yang didukung
algoritma_hash = {
    "1": ("md5", hashlib.md5),
    "2": ("sha1", hashlib.sha1),
    "3": ("sha256", hashlib.sha256),
    "4": ("sha512", hashlib.sha512)
}

animasi_delay = 0
hentikan_animasi = False

def animasi(hash_target):
    simbol = ['|', '/', '-', '\\']
    indeks_simbol = 0
    while not hentikan_animasi:
        simbol_animasi = simbol[indeks_simbol]
        sys.stdout.write(f"\rSedang memecahkan hash password {simbol_animasi}")
        sys.stdout.flush()
        indeks_simbol = (indeks_simbol + 1) % len(simbol)
        time.sleep(animasi_delay)

def hentikan_thread_animasi():
    global hentikan_animasi
    time.sleep(0)
    hentikan_animasi = True

def cek_hash(hash_target, algoritma):
    panjang_hash = len(hash_target)
    if algoritma == "md5" and panjang_hash != 32:
        return False
    elif algoritma == "sha1" and panjang_hash != 40:
        return False
    elif algoritma == "sha256" and panjang_hash != 64:
        return False
    elif algoritma == "sha512" and panjang_hash != 128:
        return False
    return True

def pemecah_hash_password():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("""
     .-.      _______
    ()``; |==|_______D   'a63e07a8a2c9df821b398df3ce7609da'
    / ('      [--|--]
(  /  |       |  |  |
 \\(_)_]]      |  |  |
-----------------------------------------------------------

                   Pemecah Hash Password
                     Dibuat oleh FII14

===========================================================
""")

    print("Algoritma hash yang didukung:")
    print("=============================")
    for i, (algoritma, _) in algoritma_hash.items():
        print(f"[{i}] {algoritma}")
    print("[K] Keluar")

    pilihan = input("\n[#] Masukkan nomor algoritma hash (1-4) atau 'K' untuk keluar: ").strip()

    if pilihan.upper() == 'K':
        print("\n[+] Keluar dari program.")
        sys.exit(0)

    try:
        algoritma, fungsi_hash = algoritma_hash[pilihan]
    except KeyError:
        print("\n[-] Masukan tidak valid.")
        sys.exit(1)

    hash_target = input("[#] Masukkan hash password: ").strip()

    if not cek_hash(hash_target, algoritma):
        print("\n[-] Hash password tidak valid.")
        sys.exit(1)

    file_wordlist = input("[#] Masukkan path ke file wordlist: ").strip()

    try:
        jumlah_seluruh_password = 0
        with open(file_wordlist, 'r', encoding='latin-1', errors='ignore') as f:
            seluruh_password = f.readlines()
            jumlah_seluruh_password = len(seluruh_password)
            print("\n[*] Menghitung jumlah password wordlist {}".format(file_wordlist))
            time.sleep(3)
            print("\r[+] Jumlah password wordlist {}: {}".format(file_wordlist, jumlah_seluruh_password))
            time.sleep(3)

        print()
        password_ditemukan = False
        jumlah_password_dicoba = 0

        # Memulai animasi
        thread_animasi = threading.Thread(target=animasi, args=(hash_target,))
        thread_animasi.start()

        for password in seluruh_password:
            time.sleep(1)
            jumlah_password_dicoba += 1
            password = password.strip()
            password_hash = fungsi_hash(password.encode('utf-8')).hexdigest()
            if password_hash == hash_target:
                password_ditemukan = True
                # Menghentikan animasi
                hentikan_thread_animasi()
                print("\n\n===========================================================")
                print("[+] Password ditemukan: {}".format(password))
                print("[+] Jenis hash: {}".format(algoritma))
                print("[+] Hash password: {}".format(hash_target))
                print("[+] Jumlah password yang dicoba: {}".format(jumlah_password_dicoba))
                print("-----------------------------------------------------------")
                break

        # Jika password tidak ditemukan, hentikan animasi
        if not password_ditemukan:
            hentikan_thread_animasi()
            print("\n\n===========================================================")
            print("[-] Password tidak ditemukan dalam wordlist.")
            print("[-] Jenis hash: {}".format(algoritma))
            print("[-] Hash password: {}".format(hash_target))
            print("[-] Jumlah password yang dicoba: {}".format(jumlah_password_dicoba))
            print("-----------------------------------------------------------")

    except FileNotFoundError:
        print("\n[-] File wordlist tidak ditemukan.")
        sys.exit(1)
    except IOError:
        print("\n[-] Kesalahan saat membaca file wordlist.")
        sys.exit(1)

try:
    pemecah_hash_password()
except KeyboardInterrupt:
    print("\n\n[-] Keluar dari program")
    hentikan_thread_animasi()
    sys.exit(0)
  
