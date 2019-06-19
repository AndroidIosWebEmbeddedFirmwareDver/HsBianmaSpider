import requests
from bs4 import BeautifulSoup

import sys

import datetime

from HsMsgPojo import HsMsgPojo
from HsMsgBaseInfoPojo import HsMsgBaseInfoPojo


# 获取网页内容
def requestTest():
    # python开发人员常用的测试地址 http://httpbin.org/gets
    response = requests.get("https://www.hsbianma.com/Code/0106329000.html")
    response.encoding = 'utf-8'
    # print(response.text)
    return response.text


# 返回顶级div#wrap
def getBodyDivWrap(soup):
    return soup.body.find(id='wrap')


# 获取wrap 下的class=hs节点
def getHSInWrapNode(soup):
    tag = getBodyDivWrap(soup).div
    return tag


# 获取内容节点
def getBaseInfoAllNode(soup):
    index = 0
    for sibling in getHSInWrapNode(soup).next_siblings:
        if index == 3:
            return sibling
        index = index + 1


# 获取基本信息
def getBaseInfoNode(soup):
    tag = getBaseInfoAllNode(soup)
    return tag.div.h3


def getBaseInfoNodeMsgNode(soup):
    tag = getBaseInfoNode(soup).find_next_sibling()
    print(tag)


def soupTest(html_doc):
    return BeautifulSoup(html_doc, 'html.parser')


if __name__ == '__main__':
    hsMagPojo = HsMsgPojo()
    # 获取全局文档
    soupHtml = soupTest(requestTest())
    # 1.获取基本信息
    hsMagPojo.setMsgName(getBaseInfoNode(soupHtml).text)
    print(hsMagPojo.getMsgName())
    # 1.1获取基本信息下的内容

    # getBaseInfoNodeMsgNode(soupHtml)
