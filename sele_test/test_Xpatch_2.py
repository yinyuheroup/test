from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def open_Chrome():
    dirver = webdriver.Chrome(r"D:\code\tpshop_test_login\dirver\chromedriver.exe")
    dirver.get('http://192.168.91.130/index.php')
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
    dirver.find_element(By.XPATH, "//*[text()='登录']").click()
    dirver.find_element(By.XPATH, '//*[@id = "username"]').send_keys(15800000001)
    dirver.find_element(By.XPATH, "//*[contains(@name,'pass')]").send_keys(123456)
    dirver.find_element(By.XPATH, "//*//div//input[@id='verify_code']").send_keys(8888)
    dirver.find_element(By.XPATH, "//*//div//a[@name='sbtbutton']").click()
    sleep(30)
    dirver.quit()


if __name__ == '__main__':
    open_Chrome()
