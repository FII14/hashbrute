#!/usr/bin/env python

import hashlib
import os
import sys
import time
import threading

# Supported hash algorithms
algoritma_hash = {
    "1": ("md5", hashlib.md5),
    "2": ("sha1", hashlib.sha1),
    "3": ("sha256", hashlib.sha256),
    "4": ("sha512", hashlib.sha512)
}

animation_delay = 0
stop_animation = False

def animate(hash_target):
    symbols = ['|', '/', '-', '\\']
    symbol_index = 0
    while not stop_animation:
        symbol = symbols[symbol_index]
        sys.stdout.write(f"\rCracking password hash {symbol}")
        sys.stdout.flush()
        symbol_index = (symbol_index + 1) % len(symbols)
        time.sleep(animation_delay)

def stop_animation_thread():
    global stop_animation
    time.sleep(0)
    stop_animation = True

def check_hash(hash_target, algorithm):
    hash_length = len(hash_target)
    if algorithm == "md5" and hash_length != 32:
        return False
    elif algorithm == "sha1" and hash_length != 40:
        return False
    elif algorithm == "sha256" and hash_length != 64:
        return False
    elif algorithm == "sha512" and hash_length != 128:
        return False
    return True

def password_cracker():
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

                   Password Hash Cracker
                     Created by FII14

===========================================================
""")

    print("Supported hash algorithms:")
    print("=============================")
    for i, (algorithm, _) in algoritma_hash.items():
        print(f"[{i}] {algorithm}")
    print("[E] Exit")

    choice = input("\n[#] Enter the hash algorithm number (1-4) or 'E' to exit: ").strip()

    if choice.upper() == 'E':
        print("\n[+] Exiting the program.")
        sys.exit(0)

    try:
        algorithm, hash_function = algoritma_hash[choice]
    except KeyError:
        print("\n[-] Invalid input.")
        sys.exit(1)

    hash_target = input("[#] Enter the hash password: ").strip()

    if not check_hash(hash_target, algorithm):
        print("\n[-] Invalid hash password.")
        sys.exit(1)

    wordlist_file = input("[#] Enter the path to the wordlist file: ").strip()

    try:
        total_passwords = 0
        with open(wordlist_file, 'r', encoding='latin-1', errors='ignore') as f:
            all_passwords = f.readlines()
            total_passwords = len(all_passwords)
            print(f"\n[*] Counting the number of passwords in the wordlist file {wordlist_file}")
            time.sleep(3)
            print(f"\r[+] Total passwords in {wordlist_file}: {total_passwords}")
            time.sleep(3)

        print()
        password_found = False
        total_passwords_tried = 0

        # Start animation
        animation_thread = threading.Thread(target=animate, args=(hash_target,))
        animation_thread.start()

        for password in all_passwords:
            total_passwords_tried += 1
            password = password.strip()
            password_hash = hash_function(password.encode('utf-8')).hexdigest()
            if password_hash == hash_target:
                password_found = True
                # Stop animation
                stop_animation_thread()
                print("\n\n===========================================================")
                print(f"[+] Password found: {password}")
                print(f"[+] Algorithm: {algorithm}")
                print(f"[+] Hash password: {hash_target}")
                print(f"[+] Total passwords tried: {total_passwords_tried}")
                print("-----------------------------------------------------------")
                break

        # If password not found, stop animation
        if not password_found:
            stop_animation_thread()
            print("\n\n===========================================================")
            print("[-] Password not found in the wordlist.")
            print(f"[-] Algorithm: {algorithm}")
            print(f"[-] Hash password: {hash_target}")
            print(f"[-] Total passwords tried: {total_passwords_tried}")
            print("-----------------------------------------------------------")

    except FileNotFoundError:
        print("\n[-] Wordlist file not found.")
        sys.exit(1)
    except IOError:
        print("\n[-] Error while reading the wordlist file.")
        sys.exit(1)

try:
    password_cracker()
except KeyboardInterrupt:
    print("\n\n[-] Exiting the program")
    stop_animation_thread()
    sys.exit(0)
