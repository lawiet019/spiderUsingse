#-*-  coding:utf-8 -*-
#主要用来测试selenium使用phantomJs

#导入webdriver
from selenium import webdriver
import time
import requests
#要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

#调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS(r"C:\Users\yufwu\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.set_window_size(1366, 768)
link_one = "http://www.bjev520.com/jsp/beiqi/pcmap/do/pcMap.jsp?chargingTypeId=&companyId=1&chargingBrandId=&brandStatuId=&cityName=北京"
driver.get(link_one)
cookie = list(driver.get_cookies())[0]["value"]

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": cookie,
"Host": "www.bjev520.com",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}
get_link_two = "http://www.bjev520.com/jsp/beiqi/pcmap/pages/pcmap_Left.jsp"
# session = requests.Session()
# session.trust_env = False
response2 = requests.get(get_link_two,headers =headers)
print(response2.text)
