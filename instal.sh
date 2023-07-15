#!/bin/bash
# Script: Instal hashbrute
# Pembuat: Rofi

g="\e[1;32m"
r="\e[0m"
c="\e[1;36m"

clear

echo -e "${c} ___ _   _ ____ _____  _    _     "
echo -e "${c}|_ _| \ | / ___|_   _|/ \  | |    "
echo -e "${c} | ||  \| \___ \ | | / _ \ | |    "
echo -e "${c} | || |\  |___) || |/ ___ \| |___ "
echo -e "${c}|___|_| \_|____/ |_/_/   \_\_____|"
echo -e "${r}"

pesan(){
    echo -e "${g}[•] ${r}Instalasi selesai."
    echo -e "${g}[•] ${r}Anda dapat menjalankannya dengan menjalankan perintah '${g}hashbrute${r}'"
}

# Fungsi untuk memeriksa keberadaan dan unduh rockyou.txt.gz jika diperlukan
rockyou(){
    if [[ -f "rockyou.txt" ]]; then
        pesan 
    else
        wget https://gitlab.com/kalilinux/packages/wordlists/-/raw/kali/master/rockyou.txt.gz
        gzip -d "rockyou.txt.gz"
        pesan
    fi
}

# Android (Termux)
if [[ $(uname -o) == "Android" ]]; then
    pkg update
    pkg install python
    pkg install wget
    pip install -r persyaratan.txt
    mv src/hashbrute /data/data/com.termux/files/usr/bin

    # Pindah ke direktori wordlists atau buat direktori jika belum ada
    direktori="/data/data/com.termux/files/usr/share/wordlists"
    if [[ -d "${direktori}" ]]; then
        cd "${direktori}"
    else
        mkdir -p "${direktori}"
        cd "${direktori}"
    fi

    rockyou
        
# Linux Ubuntu dan Debian beserta keturunannya
elif [[ $(uname -o) == "GNU/Linux" ]]; then
    sudo apt-get update 
    sudo apt-get install python3
    sudo apt-get install python3-pip
    pip3 install -r persyaratan.txt 
    mv src/hashbrute /usr/bin

    # Pindah ke direktori wordlists atau buat direktori jika belum ada
    direktori="/usr/share/wordlists"
    if [[ -d "${direktori}" ]]; then
        cd "${direktori}"
    else
        sudo mkdir -p "${direktori}"
        sudo chown -R $USER:$USER "${direktori}"
        cd "${direktori}"
    fi

    rockyou
fi
