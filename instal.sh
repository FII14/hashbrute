#!/bin/bash
# @ Script  : Instal hashbrute
# @ Pembuat : Rofi

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
chmod +x src/hashbrute

# Android (Termux)
if [[ $(uname -o) == "Android" ]]; then
    pkg update
    pkg install python3
    pip3 install -r persyaratan.txt
    mv src/hashbrute /data/data/com.termux/files/usr/bin
    mv src/token_hashbrute /data/data/com.termux/files/usr/bin
    echo -e "${g}[•] ${r}Instalasi selesai."
    echo -e "${g}[•] ${r}Anda dapat menjalankannya dengan menjalankan perintah '${g}hashbrute${r}'"
    exit 0

# Linux Ubuntu dan Debian beserta keturunannya
elif [[ $(uname -o) == "GNU/Linux" ]]; then
    sudo apt-get update 
    sudo apt-get install python3-pip
    pip3 install -r persyaratan.txt 
    mv src/hashbrute /usr/bin
    echo -e "${g}[•] ${r}Instalasi selesai."
    echo -e "${g}[•] ${r}Anda dapat menjalankannya dengan menjalankan perintah '${g}hashbrute${r}'"
    exit 0
fi
