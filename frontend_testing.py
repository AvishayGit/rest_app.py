import pymysql
import time
from selenium import webdriver

def front():
    driver = webdriver.Chrome(executable_path="S:\DevOpes H.W\chromedriver.exe")
    driver.get("http://127.0.0.1:5001/users/get_user_data/5")
    x = driver.find_element_by_xpath("//*[@id="user"]")
    print()

    time.sleep(25)


# driver.quit()



front()