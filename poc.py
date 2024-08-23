from tls_client import Session
from bs4 import BeautifulSoup


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
    session = Session(client_identifier="firefox_120", random_tls_extension_order=True)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-GPC": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }

    response = session.get("https://mas.owasp.org/contact/", headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    for data_cf_email in soup.find_all("a", {"class": "__cf_email__"}):
        obfuscated_email_address = data_cf_email.get("data-cfemail")
        email_address = n(obfuscated_email_address)
        print(email_address)

    for cf_email in soup.find_all("a"):
        cf_email = cf_email.get("href")
        if "/cdn-cgi/l/email-protection#" in cf_email:
            obfuscated_email_address = cf_email.split("#")[1]
            email_address = n(obfuscated_email_address)
            print(email_address)


if __name__ == "__main__":
    main()
