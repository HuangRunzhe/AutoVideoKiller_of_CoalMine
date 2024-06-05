from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

#账号密码
account = "140427197405191234"
key = "Hxd123456."

#Open the Chrome and URL
driver = webdriver.Chrome()
driver.get("https://study.jamg.cn/index/homePage.action")
driver.maximize_window()
print(" @@ Mission Started! @@\n")
#get INFO
title = driver.title
#Wait
driver.implicitly_wait(2)

print(title)
#Find
text_box_ID = driver.find_element(By.ID,"user")
text_box_KEY = driver.find_element(By.ID,"password")
submit_button = driver.find_element(By.ID,"login_btn")
#Type
text_box_ID.send_keys(account)
driver.implicitly_wait(2)
text_box_KEY.send_keys(key)
driver.implicitly_wait(2)


print("你有6秒时间来输入验证码")
time.sleep(5)

submit_button.click()

print("等待2秒")
time.sleep(2)

#driver.find_element(By.CSS_SELECTOR,"body > div.main > div.shortcut_area > div:nth-child(2) > div:nth-child(4)")
driver.find_element(By.XPATH,'//div[2]/div[4]')


time.sleep(5)
#text_input = driver.find_element(By.ID, "用户名")
#ActionChains(driver).send_keys_to_element(text_input, account)
#ActionChains(driver).perform()

#text_input = driver.find_element(By.ID, "密码")
#ActionChains(driver).send_keys_to_element(text_input, key)
#ActionChains(driver).perform()

for i in range(1,10):
	print("Time last:",i," s\n")
	time.sleep(1)


driver.quit()
print("Completed!")

