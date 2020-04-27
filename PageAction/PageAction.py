#! /user/bin/env  python
# -*- coding:utf-8 -*-
# renfeifei
from Utils.ObjectMap import *
from Utils.WaitUntil import *
from selenium import webdriver
from time import sleep
from Config.VarConfig import *
from Utils.Logger import log
"""
增加新action请更新VarConfig内的actionfunctions
"""
driver = None
waitUtil = None

# 打开浏览器
def openBrowser(browser):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')

    try:
        if browser.lower() == 'chrome':
            driver = webdriver.Chrome(executable_path=CHROMEPATH, chrome_options=chrome_options)
            log.logger('INFO', '===准备打开chrome浏览器===')
        else:
            driver = webdriver.Firefox(executable_path=CHROMEPATH)
            log.logger('INFO', '只下了chrome driver，你就当你打开了你要的')
    except Exception as e:
        log.logger('ERROR', '打开driver失败:{}'.format(e))
    else:
        WaitUtil = WaitUntil(driver)
    log.logger('INFO', '打开成功')

# 浏览器最大化
def maximizeBrowser():
    log.logger('INFO', '===浏览器最大化===')
    try:
        driver.maximize_window()
    except Exception as e:
        log.logger('ERROR', '最大化浏览器失败:{}'.format(e))

# 加载网址
def loadUrl(url):
    log.logger('INFO', '===载入网址===')
    log.logger('INFO', '载入网址为:{}'.format(url))
    global driver
    try:
        driver.get(url)
    except Exception as e:
        log.logger('ERROR', '载入网址失败:{}'.format(e))

# 强制等待
def sleepwait(sleepSeconds):
    log.logger('INFO', '===等待{}秒==='.format(sleepSeconds))
    try:
        sleep(int(sleepSeconds))
    except Exception as e:
        log.logger('ERROR', '等待这个动作本身失败:{}'.format(e))

# 清除输入框的内容
def clear(by, locator):
    log.logger('INFO', '===清除目标框内容===')
    log.logger('INFO', '目标定位方式为:{}'.format(by))
    log.logger('INFO', '目标定位对象为;{}'.format(locator))
    try:
        getElement(driver, by, locator).clear()
    except Exception as e:
        log.logger('ERROR', '清除内容失败:{}'.format(e))

# 输入内容
def inputValue(by, locator, value):
    log.logger('INFO', '===输入内容===')
    log.logger('INFO', '目标定位方式为:{}'.format(by))
    log.logger('INFO', '目标定位对象为:{}'.format(locator))
    log.logger('INFO', '目标对象输入内容为:{}'.format(value))
    try:
        getElement(driver, by, locator).send_keys(value)
    except Exception as e:
        log.logger('ERROR', '输入内容失败:{}'.format(e))

# 点击
def click(by, locator):
    log.logger('INFO', '===点击操作===')
    log.logger('INFO', '目标定位方式为:{}'.format(by))
    log.logger('INFO', '目标定位对象为:{}'.format(locator))
    try:
        getElement(driver, by, locator).click()
    except Exception as e:
        log.logger('ERROR', '点击失败:{}'.format(e))

# 获取页面标题
def getTitle():
    global t
    log.logger('INFO', '===获取页面标题===')
    try:
        t = driver.title
    except Exception as e:
        log.logger('ERROR', '获取页面标题:{}'.format(e))
    log.logger('INFO', '获取页面标题为:{}'.format(t))

# 切换到frame
def switchToFrame(by, locator):
    log.logger('INFO', '===切换frame===')
    log.logger('INFO', '目标定位方式为:{}'.format(by))
    log.logger('INFO', '目标定位对象为:{}'.format(locator))
    try:
        driver.switch_to_frame(getElement(driver, by, locator))
    except Exception as e:
        log.logger('ERROR', '切换frame失败:{}'.format(e))

# 返回默认frame
def switchToDefaultFrame():
    log.logger('INFO', '===切换回默认frame===')
    try:
        driver.switch_to_default_content()
    except Exception as e:
        log.logger('ERROR', '切换回默认frame失败:{}'.format(e))

# 截图
def screenshot():
    log.logger('INFO', '===截图===')
    picturename =EXCEPTPATH + f'\wu.png'
    try:
        driver.get_screenshot_as_file(picturename)
    except Exception as e:
        log.logger('ERROR', '截图失败:{}'.format(e))
    log.logger('INFO', '截图成功!存储地址为:{}'.format(picturename))

def assertbytext(by, locator, value):
    global t
    log.logger('INFO', '===验证指定元素text是否与预期结果一致===')
    try:
        t = getElement(driver, by, locator)
    except Exception as e:
        log.logger('ERROR', '获取元素失败:{}'.format(e))
    if t.text() == value:
        log.logger('INFO', '获取到元素的text为:{}'.format(t.text()))
        log.logger('INFO', '预期的text结果为:{}'.format(value))
        log.logger('INFO', '验证成功')
    else:
        log.logger('ERROR', '与预期结果不符，实际结果为:{}'.format(t.text()))
        log.logger('ERROR', '与预期结果不符，预期结果为:{}'.format(t.text()))
        log.logger('ERROR', '验证失败')

def assertbytitle(value):
    global t
    log.logger('INFO', '===验证页面标题是否与预期结果一致===')
    try:
        t = driver.title
    except Exception as e:
        log.logger('ERROR', '获取页面标题失败:{}'.format(e))
    if t == value:
        log.logger('INFO', '获取到页面标题为:{}'.format(t))
        log.logger('INFO', '预期的页面标题为:{}'.format(value))
        log.logger('INFO', '验证成功')
    else:
        log.logger('ERROR', '与预期结果不符，实际标题为:{}'.format(t))
        log.logger('ERROR', '与预期结果不符，预期标题为:{}'.format(value))
        log.logger('ERROR', '验证失败')


def assertbyTrue(by, locator):
    global t
    log.logger('INFO', '===验证指定元素存在===')
    try:
        t = getElement(driver, by, locator)
    except Exception as e:
        log.logger('ERROR', '获取元素失败:{}'.format(e))
    if t:
        log.logger('INFO', '成功获取到指定元素')
        log.logger('INFO', '验证成功')
    else:
        log.logger('ERROR', '未发现指定元素')
        log.logger('ERROR', '验证失败')


def assertbyFalse(by, locator):
    global t
    log.logger('INFO', '===验证指定元素不存在===')
    try:
        t = getElement(driver, by, locator)
    except Exception as e:
        log.logger('ERROR', '获取元素失败:{}'.format(e))
    if t:
        log.logger('INFO', '指定元素不存在')
        log.logger('INFO', '验证成功')
    else:
        log.logger('ERROR', '发现指定元素')
        log.logger('ERROR', '验证失败')


# 关闭浏览器
def quitBrowser():
    log.logger('INFO', '关闭浏览器')
    try:
        driver.quit()
    except Exception as e:
        log.logger('ERROR', '关闭浏览器失败:{}'.format(e))

if __name__ == '__main__':
    # openBrowser('Chrome')
    # loadUrl('https://mail.qq.com')
    eval("openBrowser('Chrome')")
    eval("loadUrl('https://mail.qq.com')")