import datetime
import time
from selenium import webdriver
import pymysql
now = datetime.now()
today = now.strftime("%m/%d/%y %X")
import json
import request

def Insert_post(x):
    user_name = request.post('http://127.0.0.1:5000/users/<x>' , json={"user_name: Avishay"})



def Insert_P():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='v4v77OlCF3', passwd='5EmH5HUA29', db='v4v77OlCF3')
    conn.autocommit(True)
    cursor = conn.cursor()
    request_data = request.json
    user_name = request_data.get('user_name')

    # cursor.execute("INSERT into v4v77OlCF3.users (user_id , user_name , creation_date) VALUES (6, 'Jnifir', '" + str(today) + "' )")
    cursor.execute("INSERT into v4v77OlCF3.users (user_id , user_name , creation_date) VALUES (6, 'Jnifir', '" + str(today) + "' )")
    cursor.close()
    conn.close()


def back():
    driver = webdriver.Chrome(executable_path="S:\DevOpes H.W\chromedriver.exe")
    driver.get("http://127.0.0.1:5000/users/1")
    time.sleep(3)

def test():
    driver = webdriver.Chrome(executable_path="S:\DevOpes H.W\chromedriver.exe")
    driver.get("http://127.0.0.1:5000/users/test")
    time.sleep(3)
test()