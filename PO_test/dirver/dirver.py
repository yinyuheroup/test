from selenium import webdriver


def ChromeDirver(url):
    driver = webdriver.Chrome(r'D:\code\dirver\chromedriver.exe')
    driver.maximize_window()
    return driver.get(url)



if __name__ == '__main__':
    ChromeDirver('http://192.168.91.130/index.php')