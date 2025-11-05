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

    for char in plaintext:
        if "A" <= char <= "Z":
            # Вычисляем сдвиг для текущего символа ключа
            shift = ord(keyword[key_index % key_length]) - ord("A")
            # Шифруем символ
            encrypted_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            ciphertext += encrypted_char
            key_index += 1
        elif "a" <= char <= "z":
            # Вычисляем сдвиг для текущего символа ключа
            shift = ord(keyword[key_index % key_length]) - ord("A")
            # Шифруем символ
            encrypted_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
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

    for char in ciphertext:
        if "A" <= char <= "Z":
            # Вычисляем сдвиг для текущего символа ключа
            shift = ord(keyword[key_index % key_length]) - ord("A")
            # Дешифруем символ
            decrypted_char = chr((ord(char) - ord("A") - shift + 26) % 26 + ord("A"))
            plaintext += decrypted_char
            key_index += 1
        elif "a" <= char <= "z":
            # Вычисляем сдвиг для текущего символа ключа
            shift = ord(keyword[key_index % key_length]) - ord("A")
            # Дешифруем символ
            decrypted_char = chr((ord(char) - ord("a") - shift + 26) % 26 + ord("a"))
            plaintext += decrypted_char
            key_index += 1
        else:
            # Не-буквенные символы остаются без изменений
            plaintext += char
            # ключ продолжает двигаться даже через пробелы!
            key_index += 1

    return plaintext
