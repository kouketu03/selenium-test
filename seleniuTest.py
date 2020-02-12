from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")

driver.get('https://www.google.com/')

from selenium.webdriver.common.keys import Keys
inputElement = driver.find_element_by_name("q")
#"webtechlabo"を入力します。
inputElement.send_keys("webtechlabo")
#ENTERキーを押します。
inputElement.send_keys(Keys.ENTER)


titleElements = driver.find_elements_by_class_name("LC20lb")

for titleElement in titleElements:
	titleText = titleElement.text
	print(titleText)

driver.quit()