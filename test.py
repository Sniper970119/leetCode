# -*- coding:utf-8 -*-

"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃　　　　　　　    ┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛
"""

import requests
from lxml import etree
import re

# 爬取页面的URL
url = 'https://www.baidu.com/'
# 构造请求头，反爬
headers = {
    'Host': 'www.baidu.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}


# 获取网页html
def get_html():
    res = requests.get(url=url, headers=headers)
    return res.text


def xpath_lxml(text):
    html = etree.HTML(text)
    result1 = html.xpath('//*[@id="css_index"]/text()')
    return result1


def get_image(xpath_text):
    images = re.findall('url\((.*?\.png)\)', xpath_text, re.S)
    # for image in images:
    #     return image[0]
    return images


if __name__ == '__main__':
    text = get_html()
    lists = xpath_lxml(text)  # 返回的是一个匹配到的列表
    print(lists[0])
    image = get_image(lists[0])
    print(image)
