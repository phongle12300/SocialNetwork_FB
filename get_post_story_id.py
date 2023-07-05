from parser_cookie import parseCookieRaw
import aiohttp, re

HEADERS = {
    "authority": "www.facebook.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "cache-control": "max-age=0",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "sec-ch-ua-full-version-list": '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.134", "Google Chrome";v="114.0.5735.134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"10.0.0"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "viewport-width": "852",
}


async def getPostAndStoryID(cookies: dict[str], url: str):
    async with aiohttp.ClientSession(headers=HEADERS, cookies=cookies) as session:
        async with session.get(url) as response:
            resp = await response.text()
            post_id = re.findall(r'"post_id":"(\d+)"', resp)
            storyID = re.findall(r'"storyID":"([^*"]+)"', resp)
            if post_id and storyID:
                return post_id[0], storyID[0]
    return None


import asyncio


async def test():
    cookies_raw = open("cookies.txt", "r").read().strip()
    cookies = parseCookieRaw(cookies_raw)
    post_id, storyID = await getPostAndStoryID(
        cookies,
        "https://www.facebook.com/truongnhudatt/posts/pfbid0xiAL1T1EUsJeKBVYhh7zeYQ12Aa2VLHwAE9n7C7oZdRy7JY8KzE9aBKsU7KzLEwQl",
    )
    print(post_id, storyID)


asyncio.run(test())
