from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())



#Case 1: sai pass word
# driver = webdriver.Chrome('driver/chromedriver.exe')

driver.get("http://dangky.hunre.edu.vn/cmcsoft.iu.web.info/(S(wxi0xxwa5ra554ynelfqugw4))/login.aspx")

elem = driver.find_element_by_id("txtUserName")
elem.clear()
elem.send_keys("lytuan")

elem = driver.find_element_by_id("txtPassword")
elem.clear()
elem.send_keys("123")


elem = driver.find_element_by_id("btnSubmit")
elem.send_keys(Keys.ENTER)

time.sleep(6)


elem = driver.find_element_by_id("lblErrorInfo")
assert elem.text == "Tên đăng nhập không đúng!"
driver.close()

#Case 2: dung password
# driver = webdriver.Chrome('driver/chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://dangky.hunre.edu.vn/cmcsoft.iu.web.info/(S(wxi0xxwa5ra554ynelfqugw4))/login.aspx")

elem = driver.find_element_by_id("txtUserName")
elem.clear()
elem.send_keys("test")

elem = driver.find_element_by_id("txtPassword")
elem.clear()
elem.send_keys("test_pass")


elem.send_keys(Keys.ENTER)

time.sleep(10)




driver.close()