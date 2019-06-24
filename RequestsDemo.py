import requests
from bs4 import BeautifulSoup

import json

from pojo.HsMsgPojo import HsMsgPojo
from pojo.HsMsgBaseInfoPojo import HsMsgBaseInfoPojo
from pojo.HsMsgTaxRateInformationPojo import HsMsgTaxRateInformationPojo
from pojo.HsMsgElementsOfDeclarationPojo import HsMsgElementsOfDeclarationPojo
from pojo.HsMsgRegulationConditionsPojo import HsMsgRegulationConditionsPojo
from pojo.HsMsgInspectionAndQuarantineCategoriesPojo import HsMsgInspectionAndQuarantineCategoriesPojo
from pojo.HsMsgSubordinateChaptersPojo import HsMsgSubordinateChaptersPojo
from pojo.HsMsgSubordinateChaptersChapterPojo import HsMsgSubordinateChaptersChapterPojo
from pojo.HsMsgCIQCodePojo import HsMsgCIQCodePojo
from pojo.HsMsgNaviHtmlPojo import HsMsgNaviHtmlPojo


# 序列化对象为字符串
def objectToJsonStr(mObject: object):
    return json.dumps(mObject.__dict__, ensure_ascii=False)


# 序列化嵌套对象为字符串
def nestedObjectToJsonStr(mObject: object):
    return json.dumps(mObject.__dict__, default=lambda o: o.__dict__, ensure_ascii=False)


# 反序列化嵌套字符串为对象
def JsonStrToHsMsgPojo(mStr):
    return HsMsgPojo(** json.loads(mStr))


# 获取网页
def requestTest():
    response = requests.get("https://www.hsbianma.com/Code/0106329000.html")
    response.encoding = 'utf-8'
    # print(response.text)
    return response.text


# 获取网页内容
def soupTest(html_doc):
    return BeautifulSoup(html_doc, 'html.parser')


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


# 获取基本信息内容
def getBaseInfoNodeContent(soup):
    tag = getBaseInfoNode(soup).find_next_sibling()
    # print(tag)
    # print('\n基本信息：-------------\n')
    point = 0
    mCache = HsMsgBaseInfoPojo()
    for index in tag.find_all('td'):
        if point == 1:
            mCache.productCode = index.text
        elif point == 3:
            mCache.productName = index.text
        elif point == 5:
            mCache.productCodeStatus = index.text
        elif point == 7:
            mCache.productUpdateTime = index.text
        # else:
        # print(index.text)
        point = point + 1
    print(objectToJsonStr(mCache))

    return mCache


# -------------------------------
# 获取税率信息
def getTaxRateInformationNode(soup):
    tag = getBaseInfoNode(soup).find_next_sibling().find_next_sibling().find_next_sibling()
    return tag


# 获取税率信息内容
def getTaxRateInformationContent(soup):
    tag = getTaxRateInformationNode(soup).find_next_sibling()
    # print(tag)
    # print('\n税率信息：-------------\n')
    point = 0
    mCache = HsMsgTaxRateInformationPojo()
    for index in tag.find_all('td'):
        if point == 1:
            mCache.productUnitOfMeasurement = index.text
        elif point == 3:
            mCache.productExportTariffRate = index.text
        elif point == 5:
            mCache.productExportTaxRebateRate = index.text
        elif point == 7:
            mCache.productExportTemporaryTaxRate = index.text
        elif point == 9:
            mCache.productExportVATRate = index.text
        elif point == 11:
            mCache.productExportImportPreferentialTaxRate = index.text
        elif point == 13:
            mCache.productImportTemporaryTaxRate = index.text
        elif point == 15:
            mCache.productImportCommonTaxRate = index.text
        elif point == 17:
            mCache.productConsumptionTaxRate = index.text
        # else:
        #     print(index.text)
        point = point + 1
    print(objectToJsonStr(mCache))
    return mCache


# -------------------------------
# 获取申报要素
def getElementsOfDeclarationNode(soup):
    tag = getTaxRateInformationNode(
        soup).find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()
    # print(tag)
    return tag


# 获取申报要素内容
def getElementsOfDeclarationNodeContent(soup):
    tag = getElementsOfDeclarationNode(soup).find_next_sibling()
    # print(tag)
    # print('\n申报要素：-------------\n')
    point = 0
    mCache = HsMsgElementsOfDeclarationPojo()
    for index in tag.find_all('td'):
        if point % 2 != 0:
            mCache.productElementsOfDeclaration.append(index.text)
        # else:
        #     print(index)
        point = point + 1
    print(objectToJsonStr(mCache))
    return mCache


# -------------------------------
# 获取监管条件
def getRegulationConditionsNode(soup):
    tag = getElementsOfDeclarationNode(soup).find_next_sibling().find_next_sibling().find_next_sibling()
    # print(tag)
    return tag


# 获取监管条件内容
def getRegulationConditionsNodeContent(soup):
    tag = getRegulationConditionsNode(soup).find_next_sibling()
    # print(tag)
    # print('\n监管条件：-------------\n')
    point = 0
    mCache = HsMsgRegulationConditionsPojo()
    for index in tag.find_all('td'):
        if point % 2 != 0:
            mCache.productRegulationConditions.append(index.text)
        # else:
        #     print(index)
        point = point + 1
    print(objectToJsonStr(mCache))
    return mCache


# -------------------------------
# 获取检验检疫类别
def getInspectionAndQuarantineCategoriesNode(soup):
    tag = getRegulationConditionsNode(soup).find_next_sibling().find_next_sibling().find_next_sibling()
    # print(tag)
    return tag


# 获取检验检疫类别内容
def getInspectionAndQuarantineCategoriesNodeContent(soup):
    tag = getInspectionAndQuarantineCategoriesNode(soup).find_next_sibling()
    # print(tag)
    # print('\n检验检疫类别：-------------\n')
    point = 0
    mCache = HsMsgInspectionAndQuarantineCategoriesPojo()
    for index in tag.find_all('td'):
        if point % 2 != 0:
            mCache.productInspectionAndQuarantineCategories.append(index.text)
        # else:
        #     print(index)
        point = point + 1
    print(objectToJsonStr(mCache))
    return mCache


# -------------------------------
# 获取所属章节
def getSubordinateChaptersNode(soup):
    tag = getInspectionAndQuarantineCategoriesNode(soup).find_next_sibling().find_next_sibling().find_next_sibling().h3
    # print(tag)
    return tag


# 获取所属章节内容
def getSubordinateChaptersNodeContent(soup):
    tag = getSubordinateChaptersNode(soup).find_next_sibling()
    # print(tag)
    # print('\n所属章节：-------------\n')
    point = 0
    mCache = HsMsgSubordinateChaptersPojo()
    chapter = None
    for index in tag.find_all('td'):
        if point % 2 != 0:
            chapter.name = index.text
            # mCache.chapters.append(chapter.__dict__)
            mCache.chapters.append(chapter)
        else:
            chapter = HsMsgSubordinateChaptersChapterPojo()
            chapter.code = index.text
        point = point + 1
    # print(objectToJsonStr(mCache))
    return mCache


# -------------------------------
# 获取CIQ代码(13位海关编码)
def getCIQCodeNode(soup):
    tag = getInspectionAndQuarantineCategoriesNode(
        soup).find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()
    # print(tag)
    return tag


# 获取CIQ代码(13位海关编码)内容
def getCIQCodeNodeContent(soup):
    tag = getCIQCodeNode(soup).find_next_sibling()
    # print(tag)
    # print('\nCIQ代码：-------------\n')
    point = 0
    mCache = HsMsgCIQCodePojo()
    for index in tag.find_all('td'):
        if point % 2 != 0:
            mCache.name = index.text
        else:
            mCache.code = index.text
        point = point + 1
    print(objectToJsonStr(mCache))
    return mCache


# -------------------------------
# 获取导航信息
def getNaviHtmlNode(soup):
    tag = getCIQCodeNode(soup).find_next_sibling().find_next_sibling()
    # print(tag)
    return tag


# 获取导航信息内容
def getNaviHtmlNodeContent(soup):
    tag = getNaviHtmlNode(soup)
    # print(tag)
    # print('\n导航信息：-------------\n')
    point = 0
    naviHtmls: [HsMsgNaviHtmlPojo] = []
    for index in tag.find_all('span'):
        mCache = HsMsgNaviHtmlPojo()
        mCache.name = index.text
        mCache.link = index.a['href']
        mCache.link = 'https://www.hsbianma.com' + mCache.link
        point = point + 1
        naviHtmls.append(mCache)
    # print(objectToJsonStr(naviHtmls))
    return naviHtmls


# 主方法入口
if __name__ == '__main__':
    hsMagPojo = HsMsgPojo()
    # 获取全局文档
    soupHtml = soupTest(requestTest())
    # 1.获取基本信息下的内容
    hsMagPojo.baseInfo = getBaseInfoNodeContent(soupHtml)
    # 2.获取税率信息下的内容
    hsMagPojo.taxRateInfo = getTaxRateInformationContent(soupHtml)
    # 3.获取申报信息下的内容
    hsMagPojo.elementDeclar = getElementsOfDeclarationNodeContent(soupHtml)
    # 4.获取监管条件下的内容
    hsMagPojo.regulCondition = getRegulationConditionsNodeContent(soupHtml)
    # 5.获取检验检疫类别的内容
    hsMagPojo.inspAndQuartCate = getInspectionAndQuarantineCategoriesNodeContent(soupHtml)
    # 6.获取所属章节的内容
    hsMagPojo.chapters = getSubordinateChaptersNodeContent(soupHtml)
    # 7.获取CIQ代码
    hsMagPojo.ciq = getCIQCodeNodeContent(soupHtml)
    # 8.打印全部内容
    print(nestedObjectToJsonStr(hsMagPojo))
    # getNaviHtmlNodeContent(soupHtml)
