#!/usr/bin/env python3
# encoding: utf-8
'''
@author: xxx
@license: (C) Copyright 2020, Personal exclusive right.
@contact: xxx@163.com
@software: tool
@application:
@file: mzitu_spider_multi.py
@time: 2020/6/27 22:26
@desc:
'''

# 用于抓取首页开始的多页妹子图，需与mzitu_spider_single配合

from mzitu_spider_single import *

def mzitu(start_page, end_page):
    for i in range(start_page, end_page + 1):
        url = "https://www.mzitu.com/page/" + str(i)
        # headers 直接用mzitu_spider_single里的
        response = requests.get(url=url, headers=headers)
        html = response.content
        page = etree.HTML(html)
        id = list(set(page.xpath('//ul[@id="pins"]//a/@href')))
        for j in id:
            mz_id = j[22:]
            start_work(mz_id)
            time.sleep(10)


if __name__ == '__main__':
    start = int(input('请输入起始页码：'))
    end = int(input('请输入终止页码：'))
    mzitu(start, end)
