from selenium.webdriver.support.wait import WebDriverWait


class Base:
    """
        封装:
            查找元素
            输入方法
            点击方法
            获取文本
    """

    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=10, poll_frequency=0.5):
        """
        查找元素，并使用隐式等待。
        :param loc: eg:（‘By.ID’,‘name’）
        :param timeout: 隐式等待值
        :param poll_frequency: 刷新间隔
        :return: 返回找到的元素
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(loc[0], loc[1]))

    def base_input(self, loc, value):
        """
        输入方法，传参loc，输入的值
        :param loc: eg:（‘By.ID’,‘name’）
        :param value: string
        :return:
        """

        # 获取元素
        el = self.base_find_element(loc)

        # 清空输入（避免和前次操作数据叠加）
        el.clear()

        # 输入内容
        el.send_keys(value)

    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_text(self, loc):
        return self.base_find_element(loc).text


if __name__ == '__main__':
    Base = Base
