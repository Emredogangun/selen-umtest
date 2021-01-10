from webdriver import *
import time


class TestAmazonExample(WebDriverBase):

    def __init__(self):
        super().__init__()
        self.init_driver()
        self.driver.get("https://www.hepsiburada.com/")
        #giris yap---
        self.driver.find_element_by_id("myAccount").click()
        time.sleep(2)
        self.driver.find_element_by_id("login").click()
        time.sleep(2)
        self.driver.find_element_by_id("email").send_keys("aaasssa@gmail.com")
        time.sleep(2)
        self.driver.find_element_by_id("password").send_keys("emre123")
        time.sleep(2)
        self.driver.find_element_by_css_selector("#form-login > div.form-actions > button").click()
        time.sleep(5)

       #kitap ara
        self.driver.find_element_by_xpath("//*[@id='productSearch']").send_keys("Algoritma Ve C# Programlama")
        time.sleep(2)
        self.driver.find_element_by_css_selector("#buttonProductSearch").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#productresults .search-item.not-fashion-flex .box img:first-child").click()
       # self.driver.find_element_by_xpath("//*[@id='3279cd1c-9216-453f-b97e-19cc16b1b7f5']/div/div/ul/li[1]/div/a/figure/img").click()
        time.sleep(2)
        self.driver.find_element_by_id("addToCart").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Sil").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Geri Al").click()
        time.sleep(2)








        #cıkıs yap-----
        self.driver.find_element_by_id("myAccount").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Çıkış Yap").click()








if __name__ == '__main__':
    TestAmazonExample()
    print("TEST OK")