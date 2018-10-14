import os
import re

# 下载存储路径
DIR_PATH = 'D://Pyspider_Result/zn_old/'

fileName = '18993'
print('题目id' + fileName)
if os.path.exists(DIR_PATH + fileName + ".txt"):
    with open(DIR_PATH + fileName + ".txt", 'r', encoding='utf-8') as f:
        text = f.read()
        answer = re.findall(r'\*正确选项:\n(.+)\n\*答案解析:', text, re.M | re.S)
        print(answer)
