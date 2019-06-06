from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Testbase():
    def __init__(self, driver):
        self.driver = driver

    def send_key(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def textvalue(self, locator):
        return self.driver.find_element(*locator).text

    def attributevalue(self, locator, attribute_name):
        return self.driver.find_element(*locator).get_attribute(attribute_name)

    def wait(self, locator, timeout=10, msg=None):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: self.driver.find_element(*locator), msg)

    def select(self, locator, value):
        select = Select(self.driver.find_element(*locator))
        if isinstance(value, int):
            select.select_by_index(value)
        else:
            select.deselect_by_visible_text(value)

    def open_tab(self, url):
        newwindow = 'window.open(%s);' % url
        self.driver.execute_script(newwindow)

    def finds(self, locator, index):
        return self.driver.find_elements(*locator)[index]

    def change_handle(self, index):
        handles = self.driver.window_handles
        print(handles)
        self.driver.switch_to_window(handles[index])

    def openurl(self, url):
        self.driver.get(url)

    def assertelementdisplayed(self, locator):
        try:
            result = self.driver.find_element(*locator).is_displayed()
            if result is True:
                return 1
        except:
            return 0

    def quit(self):
        self.driver.quit()
