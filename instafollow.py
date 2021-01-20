from selenium import webdriver
from time import sleep

driver=webdriver.Chrome("C:\\SERVER\\chromedriver.exe")

driver.get("https://instagram.com")
sleep(4)

#giriş bilgileri
driver.find_element_by_xpath("//input[@name='username']")\
    .send_keys("your username")
driver.find_element_by_xpath("//input[@name='password']")\
    .send_keys("your password")
driver.find_element_by_xpath("//button[@type='submit']")\
    .click()
sleep(3)

#sifrekayitiptali
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
    .click()
sleep(2)

#sifrekayitiptali
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
    .click()
sleep(2)

#bildirimiptali
driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div")\
    .click()
sleep(3)

for i in range(3): 
    for i in range(20): 
        driver.find_element_by_xpath("//button[text()='Takip Et']")\
            .click()
        sleep(5)
