from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def open_Chrome():
    dirver = webdriver.Chrome(r"D:\code\tpshop_test_login\dirver\chromedriver.exe")
    dirver.get('file:///D:/study/%E6%B5%8B%E8%AF%95/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/%E6%BA%90%E7%A0%81/9%E3%80%81%E7%AC%AC%E4%B9%9D%E9%98%B6%E6%AE%B5-UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/UI%E8%87%AA%E5%8A%A8%E5%8C%96V5.0%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/web%E7%AB%AF%E7%8E%AF%E5%A2%83/web%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/web/%E6%B3%A8%E5%86%8CA.html?userA=+1&passwordA=1&telA=2&emailA=')
    # dirver.find_element(By.LINK_TEXT,'登录').click()
    # dirver.find_element(By.ID,'userA').send_keys('admin')
    # dirver.find_element(By.ID,'passwordA').send_keys(123456)
    # dirver.find_element(By.ID,'telA').send_keys(18611111111)
    # dirver.find_element(By.ID, 'emailA').send_keys('123@qq.com')
    # dirver.find_element(By.XPATH,'//center//p[1]//input').send_keys('admin')
    # sleep(3)
    # dirver.find_element(By.XPATH,'//center//p[2]//input').send_keys(123)
    # sleep(3)
    # dirver.quit()
    '''
        css定位元素
    '''

    # dirver.find_element(By.XPATH, "//*[text()='登录']").click()
    # dirver.find_element(By.XPATH, '//*[@id = "username"]').send_keys(15800000001)
    # dirver.find_element(By.XPATH, "//*[contains(@name,'pass')]").send_keys(123456)
    # dirver.find_element(By.XPATH, "//*//div//input[@id='verify_code']").send_keys(8888)
    # dirver.find_element(By.XPATH, "//*//div//a[@name='sbtbutton']").click()

    '''
        下拉栏
    '''

    # dirver.find_element(By.CSS_SELECTOR,"[value='gz']").click()
    # sleep(3)
    # dirver.find_element(By.CSS_SELECTOR,'[value="sh"]').click()
    # sleep(3)
    # dirver.find_element(By.CSS_SELECTOR, '[value="bj"]').click()
    # sleep(30)
    # dirver.quit()

    '''
        弹框
    '''

    dirver.find_element(By.CSS_SELECTOR,"#alerta").click()
    sleep(30)
    dirver.quit()

if __name__ == '__main__':
    open_Chrome()
