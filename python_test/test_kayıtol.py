from webdriver import *
import time


class TestAmazonExample(WebDriverBase):

    def __init__(self):
        super().__init__()
        self.init_driver()
        self.driver.get("https://www.hepsiburada.com/")

        self.driver.find_element_by_id("myAccount").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Üye Ol").click()


        #uye ol-------
        self.driver.find_element_by_id("firstname").send_keys("Emre")
        time.sleep(2)
        self.driver.find_element_by_id("lastname").send_keys("Doğangün")
        time.sleep(2)
        self.driver.find_element_by_id("email-register").send_keys("e453m1re123@gmail.com")
        time.sleep(2)
        self.driver.find_element_by_id("password-register").send_keys("emre12344")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='form-user']/div[6]/button").click()
        time.sleep(2)



        #cıkıs yap-----
        self.driver.find_element_by_id("myAccount").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Çıkış Yap").click()
        #self.driver.find_element_by_xpath("//*[@id='myAccount']/div[2]/div/ul/li[6]/a").click()











if __name__ == '__main__':
    TestAmazonExample()
    print("TEST OK")