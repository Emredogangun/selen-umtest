from webdriver import *
import time


class TestAmazonExample(WebDriverBase):

    def __init__(self):
        super().__init__()
        self.init_driver()
        self.driver.get("https://www.hepsiburada.com/")
        self.driver.find_element_by_xpath("//*[@id='productSearch']").send_keys("Algoritma Ve C# Programlama")
        time.sleep(2)
        self.driver.find_element_by_css_selector("#buttonProductSearch").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#productresults .search-item.not-fashion-flex:first-child").click()

        #kitap sayfa xpath
        time.sleep(2)

        #yorum yazmayı dene--------
        self.driver.find_element_by_xpath("// *[ @ id = 'reviewsTabTrigger']").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Yorum Yap").click()
        time.sleep(2)
        #giris yap-------
        self.driver.find_element_by_id("email").send_keys("aaasssa@gmail.com")
        time.sleep(2)
        self.driver.find_element_by_id("password").send_keys("emre123")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='form-login']/div[4]/button").click()
        time.sleep(2)



        #yorum yap-----
        self.driver.find_element_by_xpath("//*[@id='rating-5']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='txtReview']").send_keys("Ben bu kitabı çok beğendim. Örnekleri basit ve güzel. Hepsiburada'ya teşekkür ediyorum.")
        time.sleep(2)
        self.driver.find_element_by_id("txtTitle").send_keys("Anlaşılır ve Kolay Anlatımlı Kitap")
        time.sleep(2)
        self.driver.find_element_by_css_selector("#addReviewContainer > div.reviews-row.text-left > div.col.lg-5.md-4.sm-3.sendReview.text-left > button").click()
        time.sleep(2)

        #cıkıs yap-----
        self.driver.find_element_by_id("myAccount").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='myAccount']/div[2]/div/ul/li[6]/a").click()




if __name__ == '__main__':
    TestAmazonExample()
    print("TEST OK")