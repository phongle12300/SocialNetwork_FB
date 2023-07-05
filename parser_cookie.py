def parseCookieRaw(cookies: str) -> dict[str]:
    result = dict()
    cookiesArr = cookies.split(";")
    cookiesArr = [cookieItem.strip() for cookieItem in cookiesArr]
    for cookieItem in cookiesArr:
        cookieItemArr = cookieItem.split("=")
        result[cookieItemArr[0]] = cookieItemArr[1]
    return result
