from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
#要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

#调用环境变量指定的PhantomJS浏览器创建浏览器对象
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.set_headless()
driver = webdriver.Chrome("C:\ProgramData\Anaconda3\Scripts\chromedriver.exe",chrome_options=option)
option.add_argument('lang=zh_CN.UTF-8')
# 更换头部
cities =["北京","上海","广州","深圳","浙江省","江苏省","广东省"]
CompanyIds=["1","5","6","4"]
for companyId in CompanyIds:
    for city in cities:
        get_link_one = "http://www.bjev520.com/jsp/beiqi/pcmap/do/pcMap.jsp?chargingTypeId=&companyId="+companyId+"&chargingBrandId=&brandStatuId=&cityName="+city
        # driver = webdriver.Chrome()
        # driver = webdriver.PhantomJS()
        driver.get(get_link_one)
        countOfKC = driver.find_element_by_id("kuaichong").text
        print(countOfKC)
        cookie = list(driver.get_cookies())[0]["value"]
        print(cookie)
        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Cookie": "JSESSIONID="+cookie,
        "Host":"www.bjev520.com",
        "Proxy-Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }

        get_link_two = "http://www.bjev520.com/jsp/beiqi/pcmap/pages/pcmap_Left.jsp"
        # session = requests.Session()
        # session.trust_env = False
        response2 = requests.get(get_link_two,headers =headers)
        response2.encoding = "utf-8"
        soup = BeautifulSoup(response2.text)
        for index,value in  enumerate(soup.ul.find_all('li')):
            number = int(soup.ul.find_all('li')[index].find('a')["href"].split("=")[1])
            print(number)
            # if number >0:
            get_link_three = "http://www.bjev520.com/jsp/beiqi/pcmap/do/pcmap_Detail.jsp?charingId="+str(number)

            response3 = requests.get(get_link_three,headers=headers)
            soup2 =  BeautifulSoup(response3.text)
            barName = soup2.find_all('div',class_='news-top')[0].find("p").text.strip()
            electFee=soup2.find_all('ul',class_='news-d details')[0].find_all("li")[1].find("div").text.split("：")[1].strip()
            rentFee = soup2.find_all('ul',class_='news-d details')[0].find_all("li")[2].find("div").text.split("：")[1].strip()
            print(barName)
            print(electFee)
            print(rentFee)
driver.quit()
print('测试完成')
