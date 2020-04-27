from selenium.webdriver.support.wait import WebDriverWait

def getElement(driver, by, locator):
    """
    查找单一元素
    :return:定位的元素对象
    """
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by, locator))
    except Exception as e:
        raise e
    else:
        return element


def getElements(driver, by, locator):
    """
    查找单一元素
    :return:定位的一组元素对象
    """
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_elements(by, locator))
    except Exception as e:
        raise e
    else:
        return elements

if __name__ == '__main__':
    from selenium import webdriver
    import time

    driver_path = f'D:\Python\chromedriver.exe'
    driver = webdriver.Chrome(driver_path)
    driver.get('https://mail.qq.com')
    time.sleep(5)
    driver.switch_to.frame('login_frame')
    time.sleep(5)
    getElement(driver, 'id', 'switcher_plogin').click()
    time.sleep(5)
    username = getElement(driver, 'id', 'u')
    username.send_keys('280496355')
