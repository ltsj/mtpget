# scrape_and_encode.py
import requests
import re
import base64


def scrape_and_encode():
    headers = {
        'authority': 'mtp.ssvip.link',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    response = requests.get('https://mtp.ssvip.link/', headers=headers)
    web_content = response.text
    proxy_links = re.findall(r'(tg://proxy\?server=[^\'"<]+)', web_content)
    combined_links = "\n".join(proxy_links)
    encoded_combined_links = base64.b64encode(combined_links.encode('utf-8')).decode('utf-8')
    return encoded_combined_links


if __name__ == "__main__":
    encoded_data = scrape_and_encode()
    with open("encoded_links.txt", "w") as file:
        file.write(encoded_data)
