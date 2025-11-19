def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()
    key_length = len(keyword)
    key_index = 0
    acapital = ord('A')
    a = ord('a')

    for char in plaintext:
        if "A" <= char <= "Z":
            # Вычисляем сдвиг для текущего символа ключа
            shift = ord(keyword[key_index % key_length]) - acapital
            # Шифруем символ
            encrypted_char = chr((ord(char) - acapital + shift) % 26 + acapital)
            ciphertext += encrypted_char
            key_index += 1
        elif "a" <= char <= "z":
            # Вычисляем сдвиг для текущего символа ключа
            shift = ord(keyword[key_index % key_length]) - acapital
            # Шифруем символ
            encrypted_char = chr((ord(char) - a + shift) % 26 + a)
            ciphertext += encrypted_char
            key_index += 1
        else:
            # Не-буквенные символы остаются без изменений
            ciphertext += char
            # ключ продолжает двигаться даже через пробелы
            key_index += 1

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()
    key_length = len(keyword)
    key_index = 0
    acapital = ord('A')
    a = ord('a')

    for char in ciphertext:
        if "A" <= char <= "Z":
            # Вычисляем сдвиг для текущего символа ключа
            shift = ord(keyword[key_index % key_length]) - acapital
            # Дешифруем символ
            decrypted_char = chr((ord(char) - acapital - shift + 26) % 26 + ord("A"))
            plaintext += decrypted_char
            key_index += 1
        elif "a" <= char <= "z":
            # Вычисляем сдвиг для текущего символа ключа
            shift = ord(keyword[key_index % key_length]) - acapital
            # Дешифруем символ
            decrypted_char = chr((ord(char) - a - shift + 26) % 26 + a)
            plaintext += decrypted_char
            key_index += 1
        else:
            # Не-буквенные символы остаются без изменений
            plaintext += char
            # ключ продолжает двигаться даже через пробелы!
            key_index += 1

    return plaintext
