from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


# driver = webdriver.Chrome('driver/chromedriver.exe')

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()