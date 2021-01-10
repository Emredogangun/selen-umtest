from webdriver import *
import time


class TestAmazonExample(WebDriverBase):
    HESAPAYARLAR_LOCATOR=(By.XPATH,"//*[@id='root']/div/div[4]/div/div[1]/div/div/div[2]/ul/li[7]/a")

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
        time.sleep(2)

        #şifremi guncelle
        self.driver.find_element_by_id("myAccount").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='myAccount']/div[2]/div/ul/li[2]/a").click()
        time.sleep(2)

        #hesap ayarlarım
        self.driver.find_element_by_css_selector(".hb-list-item:nth-child(7)").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[4]/div/div[1]/div/div/div[2]/ul/li[7]/ul/li[2]/a").click()
        time.sleep(2)
        self.driver.find_element_by_id("password").send_keys("emre123")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='form-login']/div[4]/button").click()
        time.sleep(2)

        #sifre belirleme
        self.driver.find_element_by_id("old-password").send_keys("emre123")
        time.sleep(2)
        self.driver.find_element_by_id("password").send_keys("emre1234")
        time.sleep(2)
        self.driver.find_element_by_id("password-repeat").send_keys("emre1234")
        time.sleep(2)
        self.driver.find_element_by_id("btn-update-password").click()
        time.sleep(2)






        #cıkıs yap-----
        self.driver.find_element_by_id("myAccount").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Çıkış Yap").click()








if __name__ == '__main__':
    TestAmazonExample()
    print("TEST OK")