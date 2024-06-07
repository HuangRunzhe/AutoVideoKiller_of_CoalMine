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

driver.switch_to.frame('myIframe')
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[4]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='allState']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='cs_list']/li[1]/div[1]/img").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='odiv_8834']/div/div/span[2]/table/tbody/tr[4]/td/input").click()
#driver.find_element(By.XPATH,"")

for i in range(1,5):
	address = "//*[@id='section7667']/div/h4[" + str(i) + "]/img"
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

//*[@id="section7667"]/div/h4[1]/img
//*[@id="section7667"]/div/h4[2]/img
//*[@id="section7674"]/div/h4[4]/img