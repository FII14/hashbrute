#!/usr/bin/env python

import hashlib
import os
import sys
import time
import threading
from colorama import Fore

# Kode warna
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
c = Fore.LIGHTCYAN_EX
p = Fore.RESET
w = Fore.LIGHTWHITE_EX
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX

# Algoritma hash yang didukung
algoritma_hash = {
    "1": ("md5", hashlib.md5),
    "2": ("sha1", hashlib.sha1),
    "3": ("sha224", hashlib.sha224),
    "4": ("sha256", hashlib.sha256),
    "5": ("sha384", hashlib.sha384),
    "6": ("sha512", hashlib.sha512),
    "7": ("blake2b", hashlib.blake2b),
    "8": ("blake2s", hashlib.blake2s),
    "9": ("sha3_224", hashlib.sha3_224),
    "10": ("sha3_256", hashlib.sha3_256),
    "11": ("sha3_384", hashlib.sha3_384),
    "12": ("sha3_512", hashlib.sha3_512),
    "13": ("shake_128", hashlib.shake_128),
    "14": ("shake_256", hashlib.shake_256)
}

animation_delay = 0
stop_animation = False

def animate(hash_target):
    """
    Fungsi untuk menampilkan animasi saat memecahkan hash password.

    Args:
        hash_target (str): Hash target yang akan dipecahkan.
    """
    symbols = ['|', '/', '-', '\\']
    symbol_index = 0
    while not stop_animation:
        symbol = symbols[symbol_index]
        sys.stdout.write(f"\r{w}[{y}*{w}] Sedang memecahkan hash password {symbol}{p}")
        sys.stdout.flush()
        symbol_index = (symbol_index + 1) % len(symbols)
        time.sleep(animation_delay)

def stop_animation_thread():
    """
    Fungsi untuk menghentikan animasi.
    """
    global stop_animation
    time.sleep(0)
    stop_animation = True

def check_hash(hash_target, algoritma):
    hash_length = len(hash_target)
    if algoritma == "md5" and hash_length != 32:
        return False
    elif algoritma == "sha1" and hash_length != 40:
        return False
    elif algoritma == "sha224" and hash_length != 56:
        return False
    elif algoritma == "sha256" and hash_length != 64:
        return False
    elif algoritma == "sha384" and hash_length != 96:
        return False
    elif algoritma == "sha512" and hash_length != 128:
        return False
    elif algoritma == "blake2b" and hash_length != 128:
        return False
    elif algoritma == "blake2s" and hash_length != 64:
        return False
    elif algoritma == "sha3_224" and hash_length != 56:
        return False
    elif algoritma == "sha3_256" and hash_length != 64:
        return False
    elif algoritma == "sha3_384" and hash_length != 96:
        return False
    elif algoritma == "sha3_512" and hash_length != 128:
        return False
    elif algoritma == "shake_128" and hash_length != 64:
        return False
    elif algoritma == "shake_256" and hash_length != 128:
        return False
    return True

def pemecah_hash_password():
    """
    Fungsi utama untuk memecahkan hash password.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(f"""{c}
{y}     .-.      _______
{y}    ()``; |==|_______D   {r}'a63e07a8a2c9df821b398df3ce7609da'
{y}    / ('      [--|--]
{y}(  /  |       |  |  |
{y} \\(_)_]]      |  |  |
{c}-----------------------------------------------------------

{w}                   Pemecah Hash Password
{w}                     Dibuat oleh FII14

{c}==========================================================={p}
{p}""")

    print(f"{g}Algoritma hash yang didukung{w}:")
    print("=============================")
    for i, (algoritma, _) in algoritma_hash.items():
        print(f"[{y}{i}{w}] {algoritma}")
    print(f"[{r}K{w}] Keluar")

    pilihan = input(f"\n[{b}#{w}] Masukkan nomor algoritma hash (1-14) atau 'K' untuk keluar: ").strip()

    if pilihan.upper() == 'K':
        print(f"\n[{g}+{w}] Keluar dari program.")
        sys.exit(0)

    try:
        algoritma, fungsi_hash = algoritma_hash[pilihan]
    except KeyError:
        print(f"\n[{r}-{w}] Masukan tidak valid.")
        sys.exit(1)

    hash_target = input(f"[{b}#{w}] Masukkan hash password: ").strip()

    if not check_hash(hash_target, algoritma):
        print(f"\n[{r}-{w}] Hash password tidak valid.")
        sys.exit(1)

    file_wordlist = input(f"[{b}#{w}] Masukkan path ke file wordlist: ").strip()

    try:
        jumlah_seluruh_password = 0
        with open(file_wordlist, 'r', encoding='latin-1', errors='ignore') as f:
            seluruh_password = f.readlines()
            jumlah_seluruh_password = len(seluruh_password)
            print(f"\n{w}[{y}*{w}] Menghitung jumlah password wordlist {file_wordlist}{p}")
            time.sleep(3)
            print(f"\r{w}[{g}+{w}] Jumlah password wordlist {file_wordlist}: {jumlah_seluruh_password}{p}")
            time.sleep(3)

        print()
        password_ditemukan = False
        jumlah_password_dicoba = 0

        # Memulai animasi
        animation_thread = threading.Thread(target=animate, args=(hash_target,))
        animation_thread.start()

        for password in seluruh_password:
            jumlah_password_dicoba += 1
            password = password.strip()
            password_hash = fungsi_hash(password.encode('utf-8')).hexdigest()
            if password_hash == hash_target:
                password_ditemukan = True
                # Menghentikan animasi
                stop_animation_thread()
                print(f"\n\n{c}==========================================================={p}")
                print(f"{w}[{g}+{w}] Password ditemukan: {password}{p}")
                print(f"{w}[{g}+{w}] Jenis hash: {algoritma}{p}")
                print(f"{w}[{g}+{w}] Hash password: {hash_target}{p}")
                print(f"{w}[{g}+{p}] Jumlah password yang dicoba: {jumlah_password_dicoba}{p}")
                print(f"{c}-----------------------------------------------------------{p}")
                break

        # Jika password tidak ditemukan, hentikan animasi
        if not password_ditemukan:
            stop_animation_thread()
            print(f"\n\n{c}==========================================================={p}")
            print(f"{w}[{r}-{w}] Password tidak ditemukan dalam wordlist.{p}")
            print(f"{w}[{r}-{w}] Jenis hash: {algoritma}{p}")
            print(f"{w}[{r}-{w}] Hash password: {hash_target}{p}")
            print(f"{w}[{r}-{w}] Jumlah password yang dicoba: {jumlah_password_dicoba}{p}")
            print(f"{c}-----------------------------------------------------------{p}")

    except FileNotFoundError:
        print(f"\n{w}[{r}-{w}] File wordlist tidak ditemukan.")
        sys.exit(1)
    except IOError:
        print(f"\n{w}[{r}-{w}] Kesalahan saat membaca file wordlist.")
        sys.exit(1)

try:
    # Memanggil fungsi utama
    pemecah_hash_password()
except KeyboardInterrupt:
    print(f"\n\n{w}[{r}-{w}] Keluar dari program {p}")
    stop_animation_thread()
    sys.exit(0)