
'''

[task_local]
0 6 10 * * * https://github.com/zijiahong/bilibili/blob/9a4903b90efb165798dac8963d4fd5c2d595185b/config.json

'''


import os
os.system("java -jar /ql/repo/zijiahong_bilibili/BILIBILI-HELPER.jar /ql/repo/zijiahong_bilibili/config.json")
