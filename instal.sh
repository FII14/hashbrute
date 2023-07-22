#!/usr/bin/env python3
# @ Script  : Instal hashbrute
# @ Pembuat : Rofi

from sys import platform
import os
import shutil
import requests
import gzip

g = "\033[1;32m"
r = "\033[0m"
c = "\033[1;36m"

def clear_screen():
    os.system("clear" if platform != "win32" else "cls")

def display_header():
    print(f"{c} ___ _   _ ____ _____  _    _     ")
    print(f"{c}|_ _| \ | / ___|_   _|/ \  | |    ")
    print(f"{c} | ||  \| \___ \ | | / _ \ | |    ")
    print(f"{c} | || |\  |___) || |/ ___ \| |___ ")
    print(f"{c}|___|_| \_|____/ |_/_/   \_\_____|")
    print(f"{r}")

def pesan():
    print(f"{g}[•] {r}Instalasi selesai.")
    print(f"{g}[•] {r}Anda dapat menjalankannya dengan menjalankan perintah 'hashbrute'")
    exit(0)

def rockyou():
    if os.path.isfile("rockyou.txt"):
        pesan()
    elif os.path.isfile("rockyou.txt.gz"):
        with gzip.open("rockyou.txt.gz", "rb") as f_in:
            with open("rockyou.txt", "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        pesan()
    elif os.path.isfile("rockyou.txt.gx") and os.path.isfile("rockyou.txt"):
        pesan()
    else:
        url = "https://gitlab.com/kalilinux/packages/wordlists/-/raw/kali/master/rockyou.txt.gz"
        response = requests.get(url, stream=True)
        with open("rockyou.txt.gz", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        with gzip.open("rockyou.txt.gz", "rb") as f_in:
            with open("rockyou.txt", "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove("rockyou.txt.gz")
        pesan()

def install_dependencies():
    if platform == "linux" or platform == "linux2":
        os.system("sudo apt-get update")
        os.system("sudo apt-get install python3")
        os.system("sudo apt-get install python3-pip")
    os.system("pip3 install -r persyaratan.txt")

def main():
    clear_screen()
    display_header()

    # Periksa dan berikan izin eksekusi pada file hashbrute
    os.system("chmod +x src/hashbrute")

    install_dependencies()

    # Android (Termux)
    if platform == "linux" and os.path.exists("/data/data/com.termux/files/usr/bin"):
        os.system("pkg update")
        os.system("pkg install python")
        os.system("pkg install wget")
        os.system("pip install -r persyaratan.txt")
        os.system("mv src/hashbrute /data/data/com.termux/files/usr/bin")

        # Periksa dan siapkan direktori wordlists
        direktori = "/data/data/com.termux/files/usr/share/wordlists"
        if os.path.exists(direktori):
            os.chdir(direktori)
            rockyou()
        else:
            os.makedirs(direktori)
            os.chdir(direktori)
            rockyou()

    # Linux Ubuntu dan Debian beserta keturunannya
    elif platform == "linux" and os.geteuid() == 0:
        os.system("sudo apt-get update")
        os.system("sudo apt-get install python3")
        os.system("sudo apt-get install python3-pip")
        os.system("pip3 install -r persyaratan.txt")
        os.system("mv src/hashbrute /usr/bin")

        # Periksa dan siapkan direktori wordlists
        direktori = "/usr/share/wordlists"
        if os.path.exists(direktori):
            os.chdir(direktori)
            rockyou()
        else:
            os.makedirs(direktori)
            os.chown(direktori, os.getuid(), os.getgid())
            os.chdir(direktori)
            rockyou()

if __name__ == "__main__":
    main()
