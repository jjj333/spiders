#!/usr/bin/env python3
# encoding: utf-8
'''
@author: xxx
@license: (C) Copyright 2020, Personal exclusive right.
@contact: xxx@163.com
@software: tool
@application:
@file: 作业（妹子图）.py
@time: 2020/6/27 22:26
@desc:
'''

# 用etree.parse加载本地html进行分析

from lxml import etree
from html import unescape
import requests


def mzitu_spider(url, file_name):
    # 构建请求
    headers = {
        "referer": "https://www.mzitu.com/",
        "user-agent": "mozilla/5.0 (windoWS NT 10.0; Win64; x64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/80.0.3987.163 safari/537.36"
    }
    # 发送请求
    response = requests.get(url=url, headers=headers)
    data = response.content
    file = '妹子图/%s.jpg' % file_name
    writefile(data, file)


def writefile(data, file_name):
    with open(file_name, 'bw') as f:
        f.write(data)
    print(file_name, '---保存完毕')


if __name__ == '__main__':
    parser = etree.HTMLParser(encoding="utf-8")
    page = etree.parse('mzitu.html', parser=parser)
    result = etree.tostring(page)
    html = unescape(result.decode())  # 转换HTML实体为中文
    # page = etree.HTML('mzitu.html')   # 单这样处理，下面无法选到想要的元素
    img_url = page.xpath('//li//img//@data-original')
    img_name = page.xpath('//li//img//@alt')

    for i in range(0, len(img_url)):
        new_img_name = str(i) + '.' + img_name[i]
        mzitu_spider(img_url[i], new_img_name)
