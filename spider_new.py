from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service = Service(executable_path="/path/to/chromedriver")
# driver = webdriver.Chrome(service=service)


def spider_new(url):
    url = url
    driver = webdriver.Chrome()
    driver.get(url)

    # 设置响应策略
    # driver.implicitly_wait(0.5)

    # 爬取页面标题
    title = driver.title
    # print(title)

    # 爬取页面源代码
    text = driver.page_source
    # print(text)

    # 爬取锚链接
    linklist = []
    linkstr = ''
    Linklinks = driver.find_elements(By.TAG_NAME,"a")
    num_empty_linklink = 0
    num_linklinks = len(Linklinks)
    for Linklink in Linklinks:
        linkurl = Linklink.get_attribute("href")
        print(linkurl)
        if linkurl == "":
            num_empty_linklink = num_empty_linklink + 1
        else:
            linklist.append(linkurl)
            linkstr = linkstr + linkurl + " "
    # print(num_linklinks)
    # print(num_empty_linklink)
    # print(len(linklist))
    # print(linklist)

    # 爬取图片链接
    piclist = []
    picstr = ''
    Imglinks = driver.find_elements(By.TAG_NAME,"img")
    num_empty_imglink = 0
    num_imglinks = len(Imglinks)
    for Imglink in Imglinks:
        imgurl = Imglink.get_attribute("src")
        if imgurl == "":
            num_empty_imglink = num_empty_imglink + 1
        else:
            piclist.append(imgurl)
            picstr = picstr + imgurl + " "
    # print(num_imglinks)
    # print(num_empty_imglink)
    # print(len(piclist))


    # 爬取脚本链接
    scriptlist = []
    scriptstr = ''
    scriptlinks = driver.find_elements(By.TAG_NAME, "script")
    num_empty_scriptlink = 0
    num_scriptlinks = len(scriptlinks)
    for scriptlink in scriptlinks:
        scripturl = scriptlink.get_attribute("src")
        if scripturl == "":
            num_empty_scriptlink = num_empty_scriptlink + 1
        else:
            scriptlist.append(scripturl)
            scriptstr = scriptstr + scripturl + " "
    # print(num_scriptlinks)
    # print(num_empty_scriptlink)
    # print(len(scriptlist))
    # print(scriptlist)


    driver.quit()
    return title,text,piclist,picstr,num_imglinks,num_empty_imglink,linklist,linkstr,num_linklinks,num_empty_linklink,scriptlist,scriptstr,num_scriptlinks,num_empty_scriptlink

url = "https://www.douban.com"
spider_new(url)