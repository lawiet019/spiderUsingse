from selenium import webdriver

try:
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    brower = webdriver.Firefox(firefox_options=fireFoxOptions)

    brower.get('http://www.baidu.com')
    print(brower.page_source)
finally:
    try:
        brower.close()
    except:
        pass
