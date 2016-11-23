from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://127.0.0.1:5000/ping")
assert "pong" in driver.page_source
driver.close()
