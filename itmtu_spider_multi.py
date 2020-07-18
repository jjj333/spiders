#!/usr/bin/env python3
# encoding: utf-8
'''
@author: xxx
@license: (C) Copyright 2020, Personal exclusive right.
@contact: xxx@163.com
@software: tool
@application:
@file: itmtu_spider_multi.py
@time: 2020/6/27 22:26
@desc:
'''

# 用于抓取搜索出来的妹子专辑（示例：http://www.itmtu.net/page/1/?s=%E7%B3%AF%E7%BE%8E%E5%AD%90），需与itmtu_spider_single配合
# “%E7%B3%AF%E7%BE%8E%E5%AD%90”为搜索关键字
from itmtu_spider_single import *

def itmtu(start_page, end_page):
    for i in range(start_page, end_page + 1):
        url = "http://www.itmtu.net/page/" + str(i) + "?s=%E7%B3%AF%E7%BE%8E%E5%AD%90"
        # headers 直接用itmtu_spider_single里的
        response = requests.get(url=url, headers=headers)
        html = response.content
        page = etree.HTML(html)
        id = list(set(page.xpath('//*[@id="index_ajax_list"]/li/a/@href')))
        for j in id:
            mz_id = j[4:9]
            print(mz_id)
            start_work(mz_id)
            time.sleep(5)


if __name__ == '__main__':
    start = int(input('请输入起始页码：'))
    end = int(input('请输入终止页码：'))
    itmtu(start, end)
