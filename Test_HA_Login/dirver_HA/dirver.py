from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def ChromeDirver(url):
    driver = webdriver.Chrome(r'C:\Users\TEST1\PycharmProjects\pythonProject\Driver\chromedriver.exe')
    driver.maximize_window()
    driver.get(url)
    return driver


if __name__ == '__main__':
    driver = ChromeDirver('https://10.12.70.226:9997/zh/login')
    # driver.find_element(By.ID, 'details-button').click()
    # sleep(3)