# -*- coding: UTF-8 -*-
# 爬虫实战

import requests
import json
from lxml import etree
from selenium import webdriver

# topic1 Requests访问页面
r = requests.get('http://www.douban.com')
r = requests.post('http://www.xxx.com', data={'key': 'value'})

# topic2 XPath定位
html = etree.HTML(html)
result = html.xpath('//li')

# topic3 JSON对象
jsonData = '{"a":1, "b":2, "c":3, "d":4, "e":5}';
input = json.loads(jsonData)
print(input)

# topic4 JSON下载海报
query = '伍迪艾伦'
'''下载图片'''
def download(src, id):
    dir = './' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')

'''for循环 请求全部的url'''
for i in range(0, 2374, 20):
    url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start='+str(i)
    html = requests.get(url).text   #得到返回结果
    response = json.loads(html, encoding='utf-8')   #将JSON格式转换成Python对象
    for image in response['images']:
        print(image['src']) #查看当前下载的图片网址
        download(image['src'], image['id']) #下载一张图片

# topic5 XPath下载海报
url = 'https://movie.douban.com/subject_search?search_text=伍迪艾伦&cat=1002'
driver = webdriver.Chrome()
driver.get(url)
html = etree.HTML(driver.page_source)
src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
srcs = html.xpath(src_xpath)
titles = html.xpath(title_xpath)
for src, title in zip(srcs, titles):
    download(src, title.text)
