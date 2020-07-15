#!/usr/bin/env python3
# encoding: utf-8
'''
@author: xxx
@license: (C) Copyright 2020, Personal exclusive right.
@contact: xxx@163.com
@software: tool
@application:
@file: mzitu_spider_single.py
@time: 2020/6/27 22:26
@desc:
'''

# 用etree.HTML在线加载网页进行分析


from lxml import etree
import requests, os, time

headers = {
        "Host": "img.itmtu.cc",
        "referer": "http://www.itmtu.net/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def mzitu_spider(url, file_name, folder):
    response = requests.get(url=url, headers=headers)
    time.sleep(1)
    data = response.content
    create_folder(folder)
    file = f'{folder}/{file_name}.jpg'
    writefile(data, file)


def writefile(data, file_name):
    with open(file_name, 'bw') as f:
        f.write(data)
    print(file_name, '---保存完毕')


def start_work(id):
    url = "http://www.itmtu.net/mm/" + id
    response = requests.get(url=url, headers=headers)
    html = response.content
    page = etree.HTML(html)
    try:
        img_last = page.xpath('//*[@id="image_div"]/div/a[7]')[-1].text
    except IndexError:
        raise '没有这个妹子！'
    except Exception as e:
        print(e)
    img_url = str(page.xpath('//*[@id="image_div"]/p/a/img/@src')[0])
    img_url_front = img_url[:-8]
    folder_name = f'爱淘美图/({id})' + page.xpath('string(//h1)')

    for i in range(1, int(img_last) + 1):
        new_img_url = img_url_front + str('%04d' % i)  + '.jpg'
        mzitu_spider(new_img_url, i, folder_name)

if __name__ == '__main__':
    id = input('请输入妹子id：')
    start_work(id)