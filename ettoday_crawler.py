#!/usr/bin/python
# #-*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from pandas import Series,DataFrame
import pandas as pd
import numpy as np 
import time
import datetime
import re

df = pd.DataFrame() #創建空間
headerlist = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
           "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]

def sport1():
    
    baseketball = ['NBA','SBL、WSBL']

    for ball in baseketball:
        for page in range(1,4):
            time.sleep(1)
            url = requests.get('https://sports.ettoday.net/news-list/'+'籃球/'+ball+'/'+str(page)).text
            soup = BeautifulSoup(url, 'html.parser')
        
            for ele in soup.find('div', 'part_pictxt_1').find_all('div','box_0 clearfix'):

                datelist = re.findall('(\d+)',ele.find('span','date').text.strip()) #利用re正規式找出時間
                del datelist[3] #刪除時分秒
                del datelist[3]
                datestr = datelist[0] + datelist[1] + datelist[2] #接成字符串

                if datestr == time.strftime("%Y%m%d"): #如果為當日就存入
                
                    a = pd.Series({"category":'運動',"title":ele.find('h3').text.strip(),"href":'https://sports.ettoday.net'+ele.find('a')['href'],"category2":ball})
                    global df
                    df = df.append(a,ignore_index = True)

    baseball = ['MLB','中職','日、韓職','國內業餘']
    for ball in baseball:
        for page in range(1,4):
            time.sleep(1)
            url = requests.get('https://sports.ettoday.net/news-list/'+'棒球/'+ball+'/'+str(page)).text
            soup = BeautifulSoup(url, 'html.parser')
        
            for ele in soup.find('div', 'part_pictxt_1').find_all('div','box_0 clearfix'):

                datelist = re.findall('(\d+)',ele.find('span','date').text.strip()) #利用re正規式找出時間
                del datelist[3] #刪除時分秒
                del datelist[3]
                datestr = datelist[0] + datelist[1] + datelist[2] #接成字符串

                if datestr == time.strftime("%Y%m%d"): #如果為當日就存入
                
                    a = pd.Series({"category":'運動',"title":ele.find('h3').text.strip(),"href":'https://sports.ettoday.net'+ele.find('a')['href'],"category2":ball})
                    df = df.append(a,ignore_index = True)

    football = ['台灣足球','國際動態']
    for ball in football:
        for page in range(1,4):
            time.sleep(1)
            url = requests.get('https://sports.ettoday.net/news-list/'+'足球/'+ball+'/'+str(page)).text
            soup = BeautifulSoup(url, 'html.parser')
        
            for ele in soup.find('div', 'part_pictxt_1').find_all('div','box_0 clearfix'):

                datelist = re.findall('(\d+)',ele.find('span','date').text.strip()) #利用re正規式找出時間
                del datelist[3] #刪除時分秒
                del datelist[3]
                datestr = datelist[0] + datelist[1] + datelist[2] #接成字符串

                #yesterday = datetime.today() + timedelta(-1)
                #yesterday_format = yesterday.strftime('%Y%m%d')

                if datestr == time.strftime("%Y%m%d"): #如果為當日就存入
                #if datestr == yesterday_format:
                    a = pd.Series({"category":'運動',"title":ele.find('h3').text.strip(),"href":'https://sports.ettoday.net'+ele.find('a')['href'],"category2":ball})
                    
                    df = df.append(a,ignore_index = True)

    test = ['技擊、球類','陸上、水上']
    for ball in test:
        for page in range(1,4):
            time.sleep(1)
            url = requests.get('https://sports.ettoday.net/news-list/'+'競技/'+ball+'/'+str(page)).text
            soup = BeautifulSoup(url, 'html.parser')
        
            for ele in soup.find('div', 'part_pictxt_1').find_all('div','box_0 clearfix'):

                datelist = re.findall('(\d+)',ele.find('span','date').text.strip()) #利用re正規式找出時間
                del datelist[3] #刪除時分秒
                del datelist[3]
                datestr = datelist[0] + datelist[1] + datelist[2] #接成字符串

                if datestr == time.strftime("%Y%m%d"): #如果為當日就存入
                
                    a = pd.Series({"category":'運動',"title":ele.find('h3').text.strip(),"href":'https://sports.ettoday.net'+ele.find('a')['href'],"category2":ball})
                    
                    df = df.append(a,ignore_index = True)

    print('運動版 Done')


def pet2():
    cate = ['寵物好萌','動物熱搜','新聞總覽']

    for page in cate:
        time.sleep(1)
        url = requests.get('https://pets.ettoday.net/focus/'+str(page)).text
        soup = BeautifulSoup(url, 'html.parser')
        
        for ele in soup.find('div', 'part_pictxt_3 lazyload').find_all('div','clearfix'):

            if len(ele.find('span','date').text.strip()) <= 5: #如果為當日就存入
           
                a = pd.Series({"category":'寵物動物',"title":ele.find('h3').text.strip(),"href":'http:'+ele.find('a')['href']})
                global df
                df = df.append(a,ignore_index = True)

    url = requests.get('https://pets.ettoday.net/video/125/').text
    soup = BeautifulSoup(url, 'html.parser')

    for ele in soup.find('div', 'part_thumb_5 clearfix').find_all('div','piece'):

        datelist = re.findall('(\d+)',ele.find('span','date').text.strip()) #利用re正規式找出時間
            
        del datelist[3] #刪除時分秒
        del datelist[3]
        del datelist[3]
        datestr = datelist[0] + datelist[1] + datelist[2] #接成字符串
        
        if datestr == time.strftime("%Y%m%d"): #如果為當日就存入
            
            a = pd.Series({"category":'寵物動物',"title":ele.find('h3').text.strip(),"href":'https:'+ele.find('a')['href']})
            
            df = df.append(a,ignore_index = True)

    print('寵物版 Done')




def ettodayhl7():
    
    cate = ['美體','健康焦點','醫藥新聞','飲食']

    for page in cate:
        time.sleep(1)
        for temp in range(1,3):
            url = requests.get('https://health.ettoday.net/category/'+page+'/'+str(temp)).text
            soup = BeautifulSoup(url, 'html.parser')
            for ele in soup.find('div', 'part_pictxt_1').find_all('div','clearfix'):

                datelist = re.findall('(\d+)',ele.find('span','date').text.strip()) #利用re正規式找出時間

                del datelist[3] #刪除時分秒
                del datelist[3]
                del datelist[3]
            
                datestr = datelist[0] + datelist[1] + datelist[2] #接成字符串
            

                if datestr == time.strftime("%Y%m%d"): #如果為當日就存入
           
                    a = pd.Series({"category":'健康',"title":ele.find('h3').text.strip(),"href":ele.find('a')['href']})
                    global df
                    df = df.append(a,ignore_index = True)
    print('健康版 Done')


def ettodayhot8():
    #ettoday動態網頁
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://www.ettoday.net/news/news-list.htm")

    for i in range (1,5):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #向下捲動
        time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    for ele in soup.find('div', 'part_list_2').find_all('h3'):
        
        datelist = re.findall('(\d+-*\d*)',ele.find('span','date').text.strip()) #利用re正規式找出時間
    
        del datelist[3] #刪除時分秒
        del datelist[3]
        
            
        datestr = datelist[0] + datelist[1] + datelist[2] #接成字符串
            

        if datestr == time.strftime("%Y%m%d"): #如果為當日就存入
        
            a = pd.Series({"category":ele.find('em').text.strip(),"title":ele.find('a').text.strip(),"href":'https://www.ettoday.net/'+ele.find('a')['href']})
            global df
            df = df.append(a,ignore_index = True)
    driver.close()
    print('ET新聞總攬 Done')


def international9():
    #et動態國際新聞
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://www.ettoday.net/news/focus/%E5%9C%8B%E9%9A%9B/")

    for i in range (1,10):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #向下捲動
        time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    for ele in soup.find('div', 'part_pictxt_3 lazyload').find_all('div','piece clearfix'):
        
        if len(ele.find('span','date').text.strip()) <= 5: #如果為當日就存入
           
            a = pd.Series({"category":'國際',"title":ele.find('h3').text.strip(),"href":'https://www.ettoday.net'+ele.find('a')['href']})
            global df
            df = df.append(a,ignore_index = True)
    driver.close()
    print('國際板 Done')



if __name__ == '__main__':

    
    
        
    sport1()
    pet2()
    ettodayhl7()
    ettodayhot8()
    international9()
    

    print(df) # 看看資料框的外觀

    df.to_csv('Result.txt')