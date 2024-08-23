def r(e: str, t: int) -> int:
    r = e[t : 2 + t]
    return int(r, 16)


def n(n: str, c: int = 0) -> str:
    o = ""
    a = r(n, c)
    for i in range(2, len(n), 2):
        l = r(n, i) ^ a
        o += chr(l)
    return o


def main():
    obfuscated_email_address = "531032213f3c207d1b3c3f3426362132133c243220237d3c2134"
    email_address = n(obfuscated_email_address)
    print(email_address)


if __name__ == "__main__":
    main()
