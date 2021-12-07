#-*- codeing = utf-8 -*-
#@Time: 2021/12/7 21:28
#@Auther: Jack hou
#@File: YouMeiTu.py
#@Software: PyCharm

import requests
from bs4 import BeautifulSoup
import time
import os

main_page_content = requests.get("http://www.umei.cc/meinvtupian/meinvxiezhen/")

main_page = BeautifulSoup(main_page_content.text, "html.parser")
n = 1
alist = main_page.find("div", attrs={"class": "TypeList"}).find_all("a", attrs={"class": "TypeBigPics"})
for a in alist:
    #发送请求到子页面，进入小姐姐页面
    child_url = "https://www.umei.cc"+a.get("href")
    # print(child_url)
    resp = requests.get(child_url)
    resp.encoding="utf-8"
    # # print(resp.text)

    child_page = BeautifulSoup(resp.text, "html.parser")
    # 找到图片真实路径
    img = child_page.find("div", attrs={"class": "ImageBody"}).find("img")
    # print(img)
    basename = child_page.find("strong").text
    open(f"img/tu{n}.jpg", "wb").write(requests.get(img.get("src")).content)
    n += 1
    print(f"下载{n}张图片了")
    # script = img.find_next("script")
    # all_pages = int(script.text.split(",")[1].strip("\""))#找到“12”并干掉两边的引号
    # print(all_pages)
    # time.sleep(1)
    # for i in range(2, all_pages+1):
    #     grand_child_url = child_url.replace(".htm", "_"+str(i)+".htm")
    #     grand_html = requests.get(url=grand_child_url)
    #     grand_html.encoding="utf-8"
    #     grand_page = BeautifulSoup(grand_html.text, "html.parser")
    #     # print(grand_page)
    #     grand_img = grand_page.find("div", attrs={"class": "NewPages"}).find("img")
    #     open(f"img/tu{n}.jpg", "wb").write(requests.get(grand_img.get("src")).content)
    #     n += 1
    #     print(f"下载{n}张图片了")
    #     time.sleep(1)
    #

