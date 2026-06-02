try:
    file_in = open('secret.txt', 'r', encoding='utf-8')
    original_text = file_in.read()
    file_in.close()

    encrypted_text = ""
    for char in original_text:
        if char.isalpha():
            encrypted_text += chr(ord(char) + 3)
        else:
            encrypted_text += char

    file_enc = open('encrypted.txt', 'w', encoding='utf-8')
    file_enc.write(encrypted_text)
    file_enc.close()
    print("Текст зашифрован и сохранен в encrypted.txt")

    file_enc_read = open('encrypted.txt', 'r', encoding='utf-8')
    text_to_decrypt = file_enc_read.read()
    file_enc_read.close()

    decrypted_text = ""
    for char in text_to_decrypt:
        if char.isalpha():
            decrypted_text += chr(ord(char) - 3)
        else:
            decrypted_text += char

    file_dec = open('decrypted.txt', 'w', encoding='utf-8')
    file_dec.write(decrypted_text)
    file_dec.close()
    print("Текст расшифрован и сохранен в decrypted.txt")

except FileNotFoundError:
    print("Ошибка: Файл secret.txt не найден.")