import hashlib

def login():
    while True:
        token = input("Masukkan token: ")

        if verify_token(token):
            hashbrute
            break
        else:
            print("Token tidak valid. Silakan coba lagi.")

def verify_token(token):
    token_valid = "5825a233e433be57f553b127ee3ee498"
    token_encrypted = hashlib.md5(token.encode()).hexdigest()

    return token_encrypted == token_valid

login()
