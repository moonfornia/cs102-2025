def encrypt_transposition(plaintext: str, block_size: int, id1: int, id2: int) -> str:
    if id1 >= block_size or id2 >= block_size:
        raise ValueError("indices greater than block size")

    result = ""
    length = len(plaintext)

    for i in range(0, length, block_size):
        block = list(plaintext[i : i + block_size])

        if len(block) == block_size:
            block[id1], block[id2] = block[id2], block[id1]

        result += "".join(block)

    return result
