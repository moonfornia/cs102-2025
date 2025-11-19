def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    a = ord("a")
    acapital = ord("A")
    ciphertext = ""
    for ch in plaintext:
        if "a" <= ch <= "z":
            ciphertext += chr((ord(ch) - a + shift) % 26 + a)
        elif "A" <= ch <= "Z":
            ciphertext += chr((ord(ch) - acapital + shift) % 26 + acapital)
        else:
            ciphertext += ch

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    a = ord("a")
    acapital = ord("A")
    plaintext = ""
    for ch in ciphertext:
        if "a" <= ch <= "z":
            plaintext += chr((ord(ch) - a - shift) % 26 + a)
        elif "A" <= ch <= "Z":
            plaintext += chr((ord(ch) - acapital - shift) % 26 + acapital)
        else:
            plaintext += ch
    return plaintext
