print("Введите сообщение: ")
message = input()
print("Введите ключ: ")
shift = input()
print("Введенная строка: ", message)


def encrypt_caesar(msg: str, shift: int = 3) -> str:
    result = ""
    for i in msg:
        result += chr(ord(i)+shift)
    return result


def decrypt_caesar(msg: str, shift: int = 3) -> str:
    result = ""
    for i in msg:
        result += chr(ord(i)-shift)
    return result


encrypt_message = encrypt_caesar(message, 3)
print("Зашифрованная строка", encrypt_message)
decrypt_message = decrypt_caesar(encrypt_message, 3)
print("Расшифрованная строка", decrypt_message)