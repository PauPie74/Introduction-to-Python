def dec_to_hex(n):
    digits = "0123456789ABCDEF"
    x = (n % 16)
    rest = n // 16
    if (n == 0):
        return digits[x]
    dec_to_hex(rest)
    print(digits[x],end="")