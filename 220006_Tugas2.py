# Nama : Muhammad Nefrit Mahardika
# NPM : 140810220006
# Deskripsi : Tugas 2 Kriptografi 
def encrypt(text, shift):
    result = ""

    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    shift = int(input("Masukkan shift(K): "))
    text = input("Masukan teks anda: ")

    encrypted_text = encrypt(text, shift)
    print("Teks sudah terenkripsi!:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, shift)
    print("Teks sudah terdekripsi!:", decrypted_text)
