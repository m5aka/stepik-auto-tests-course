from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
	browser.get('http://suninjuly.github.io/explicit_wait2.html')
	opt_price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
	)

	browser.find_element_by_id('book').click()
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	input_answer = browser.find_element_by_id("answer")
	input_answer.send_keys(y)
	btn = browser.find_element_by_id('solve').click()
	time.sleep(30)

finally:
	browser.quit()