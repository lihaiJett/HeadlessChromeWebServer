from selenium import webdriver
from time import sleep  #导入等待 无比重要的等待
import json
import os
#下载存储路径
DIR_PATH = 'D://Pyspider_Result/zn_old/'

browser = webdriver.Chrome()
browser.get('https://ancient.fenbi.com/login')
with open('cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
for cookie in listCookies:
    browser.add_cookie({
        'domain': cookie['domain'],
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None
    })

# sleep(3)
# browser.find_element_by_id("loginphone").send_keys("15089963099")
# browser.find_element_by_id("loginpassword").send_keys("x15089963099")
# sleep(1)
# browser.find_element_by_partial_link_text('立即登录').click()
# sleep(2)
#
# cookies = browser.get_cookies()
# jsonCookies = json.dumps(cookies)
# with open('cookies.json', 'w') as f:
#     f.write(jsonCookies)


browser.get('https://ancient.fenbi.com/xingce')
browser.find_element_by_css_selector("[class='btn btn-primary select-csk']").click()
sleep(1)
browser.find_elements_by_css_selector("[class='sprite sprite-expand i-20']")[7].click()
sleep(1)
for a in browser.find_elements_by_css_selector("[class='btn btn-round create-exercise']"):
    if '13849' == a.get_attribute("data-keypoint-id"):
        print(a.get_attribute("data-keypoint-id"))
        a.click()
        break

sleep(1)
# 填答案
for question_option in browser.find_elements_by_css_selector('.option.correct'):#
    print(question_option.text)
    question_option.click()
# 交卷
browser.find_element_by_css_selector(".commit-exercise.last").click()
sleep(1)
try:
    browser.find_element_by_css_selector(".btn.btn-paper.btn-paper-xlarge.submit").click()
except Exception  as e:
    print (e)
sleep(1)
browser.find_element_by_partial_link_text('查看解析').click()
