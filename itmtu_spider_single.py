#!/usr/bin/env python3
# encoding: utf-8
'''
@author: xxx
@license: (C) Copyright 2020, Personal exclusive right.
@contact: xxx@163.com
@software: tool
@application:
@file: itmtu_spider_single.py
@time: 2020/6/27 22:26
@desc:
'''

# 用etree.HTML在线加载网页进行分析


from lxml import etree
import requests, os, time, re

headers = {
    "referer": "http://www.itmtu.net/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

mark = 0    # 判断抓取的内容是否html的标记
def itmtu_spider(url, file_name, folder):
    response = requests.get(url=url, headers=headers)
    data = response.content
    global mark
    if b'<!DOCTYPE' in data:    # 如果存在“<!DOCTYPE”则说明未取到正确的图片内容
        mark = 1
    else:
        mark = 0

    if not os.path.exists(folder):
        os.makedirs(folder)
    file = f'{folder}/{file_name}.jpg'
    writefile(data, file)


def writefile(data, file_name):
    with open(file_name, 'bw') as f:
        f.write(data)
    print(file_name, '---保存完毕')


def start_work(id):
    time.sleep(0.3)
    url = "http://www.itmtu.net/mm/" + id
    response = requests.get(url=url, headers=headers)
    html = response.content
    page = etree.HTML(html)
    try:
        img_last = page.xpath('//*[@id="image_div"]/div/a[7]')[-1].text     # 提取页码
        print(img_last)
    except IndexError:
        raise '没有这个妹子！'
    except Exception as e:
        print(e)

    folder_name = f'爱淘美图/({id})' + page.xpath('string(//h1)')
    img_url = str(page.xpath('//*[@id="image_div"]/p/img/@src')[0])     # 图片路径会变
    print(img_url)
    img_url_front = img_url[:-8]

    for img_id in range(1, int(img_last) + 1): #
        new_img_url = img_url_front + str('%03d' % img_id) + '.jpg'
        itmtu_spider(new_img_url, img_id, folder_name)
        if mark == 1:
            new_img_url = img_url_front + str('%04d' % img_id) + '.jpg'
            itmtu_spider(new_img_url, img_id, folder_name)



if __name__ == '__main__':
    id = input('请输入妹子id：')
    start_work(id)
