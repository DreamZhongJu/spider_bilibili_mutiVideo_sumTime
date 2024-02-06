'''
在最下面输入你想获得的起始和末尾分p
'''
from selenium import webdriver
from time import sleep
import re


class openEdge():
    def __init__(self,URL = None):
        self.URL = URL
        browserOption = webdriver.EdgeOptions()
        browserOption.add_argument('--headless')
        browserOption.add_argument('--mute-audio')
        self.browser = webdriver.Edge(browserOption)
        self.browser.get(URL)

    def getTime(self,sleepTime=3,start=1,end=None,pattern = None):
        sleep(sleepTime)
        try:
            duration = self.browser.find_element("class name", "cur-list")
            regex = re.compile(pattern)
            matches = regex.findall(duration.text)
        except:
            print("元素获取失败")


        mine = 0
        sec = 0
        if end == None:
            end = len(matches) - 1
        try:
            for i in matches[start - 1:end]:
                mine += int(i[0])
                # print(f'{i[0]}->{mine}')
                sec += int(i[1])
            mine += sec // 60
            sec = sec % 60
            print(f"该视频从p{start}到p{end}的总时长为{mine}:{sec}")
        except:
            print(f"该视频不是多p视频或子视频数不是{end-start+1}，抓取失败！")
        self.browser.quit()



if __name__ == '__main__':
    openEdge('(在这里输入你的b站多p视频网址)').getTime(start=1,end = 5,pattern=r"\b(\d{2}):(\d{2})\b")
