import aiohttp


# Set up the proxy with authentication
async def check_proxy(proxy_host, proxy_port, proxy_username, proxy_password):
    proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                "https://www.example.com", proxy=proxy_url, timeout=5
            ) as response:
                if response.status == 200:
                    return True
                else:
                    return False
        except aiohttp.ClientError:
            return False
