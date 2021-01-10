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
        self.driver.find_element_by_xpath("//*[@id='form-login']/div[4]/button").click()
        time.sleep(5)

       #kitap 1
        self.driver.find_element_by_xpath("//*[@id='productSearch']").send_keys("Algoritma Ve C# Programlama")
        time.sleep(2)
        self.driver.find_element_by_css_selector("#buttonProductSearch").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#productresults .search-item.not-fashion-flex .box img:first-child").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/main/div[4]/section[1]/div[4]/div/div[4]/div[1]/div[7]/ul/li[2]/a").click()
        time.sleep(5)

        # kitap ara2
        self.driver.find_element_by_xpath("//*[@id='pcwrapper']/div/i").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='productSearch']").send_keys("Algoritma Ve C# Programlama")
        time.sleep(5)
        self.driver.find_element_by_css_selector("#buttonProductSearch").click()
        time.sleep(5)
        self.driver.find_element_by_css_selector("#productresults .search-item.not-fashion-flex:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/main/div[4]/section[1]/div[4]/div/div[4]/div[1]/div[7]/ul/li[2]/a").click()
        time.sleep(5)

        #karsilastir
        self.driver.find_element_by_xpath("//*[@id='pcwrapper']/div/div[2]").click()

        #cıkıs yap-----
        self.driver.find_element_by_id("myAccount").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Çıkış Yap").click()








if __name__ == '__main__':
    TestAmazonExample()
    print("TEST OK")