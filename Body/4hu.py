#-*- codeing = utf-8 -*-
#@Time: 2021/12/8 22:19
#@Auther: Jack hou
#@File: 4hu.py
#@Software: PyCharm

import requests
from bs4 import BeautifulSoup
import time
import os
# 主页面
main_page_content = requests.get("https://www.4hu.tv/pic/toupai/")
main_page_content.encoding = 'utf-8'
main_page = BeautifulSoup(main_page_content.text, "html.parser")
# print(main_page)
# 子页面
# 找分类图片的标签

div=main_page.find("div",class_="row col6 clearfix")
# print(div)

# 找dt标签
# dt=div.find_all("dt")
# print(dt)
# print(len(dt))
# print(dt.href.string)
# href=dt.find("href")
# print(href)
# print(dt['href'])


# 提取a标签
# a=div.find_all("a")
# print(a)
list1=div.find_all('a')
list2=list1[::2]
n=0
for k in list2:
    child_href="https://www.4hu.tv"+k['href']
    # print(body_href)
    resp = requests.get(child_href)
    resp.encoding = 'utf-8'
    child_page = BeautifulSoup(resp.text, "html.parser")
# print(child_page)
#     print(child_page.text)
    img = child_page.find("div", attrs={"class": "pic"}).find("img")
    # print(img)
    open(f"img/tu{n}.jpg", "wb").write(requests.get(img.get("src")).content)
    n += 1
    print(f"下载{n}张图片了")
# a=dt.get('a')
# print(a)
# child_page=requests.get
# resp = requests.get()
#
#  resp.encoding='utf-8'
#  child = BeautifulSoup(resp.text,"html.parser")
#  div = child.find("div",class_="ImageBody")
#  img = div.find("img")
# main_page.encoding="utf-8"
# index1=main_page.find("div", attrs={"class": " row col6 clearfix"})
# child_url = index1.get("href")
# main_page.encoding="utf-8"
# print(child_url)
# child_url = index1.get("href")
# print(child_url)
# for a in alist:
#     #发送请求到子页面，进入小姐姐页面
#     child_url = a.get("href")
#     # print(child_url)
#     resp = requests.get(child_url)
#     resp.encoding="utf-8"
#     # # print(resp.text)

#     child_page = BeautifulSoup(resp.text, "html.parser")
#     # 找到图片真实路径
#     img = child_page.find("div", attrs={"class": "ImageBody"}).find("img")
#     # print(img)
#     basename = child_page.find("strong").text
#     open(f"img/tu{n}.jpg", "wb").write(requests.get(img.get("src")).content)
#     n += 1
#     print(f"下载{n}张图片了")
#     # script = img.find_next("script")
#     # all_pages = int(script.text.split(",")[1].strip("\""))#找到“12”并干掉两边的引号
#     # print(all_pages)
#     # time.sleep(1)
#     # for i in range(2, all_pages+1):
#     #     grand_child_url = child_url.replace(".htm", "_"+str(i)+".htm")
#     #     grand_html = requests.get(url=grand_child_url)
#     #     grand_html.encoding="utf-8"
#     #     grand_page = BeautifulSoup(grand_html.text, "html.parser")
#     #     # print(grand_page)
#     #     grand_img = grand_page.find("div", attrs={"class": "NewPages"}).find("img")
#     #     open(f"img/tu{n}.jpg", "wb").write(requests.get(grand_img.get("src")).content)
#     #     n += 1
#     #     print(f"下载{n}张图片了")
#     #     time.sleep(1)
#     #

