def r(e: str, t: int) -> str:
    r = e[t:2 + t]
    return int(r, 16)


def n(n: str, c: int) -> str:
    o = ""
    a = r(n, c)
    for i in range(2, len(n), 2):
        l = r(n, i) ^ a
        o += str(chr(l))
    return o


def main():
    obfuscated_email_address = "c7a6a6beb2b4af87a6b2b5a8b5a6a8b4b4e9a4a8aa"
    email_address = n(obfuscated_email_address, 0)
    print(email_address)


if __name__ == "__main__":
    main()
