
'''

[task_local]
0 6 10 * * * bilibili_run.py, tag=bilbili 定时签到, enabled=true
'''


import os

if  os.path.exists("/ql/scripts/bilibili_config.json") == False:
    os.system("cp /ql/repo/zijiahong_bilibili/config.json  /ql/scripts/bilibili_config.json")
    print("bilibili_config.json 配置文件不存在,已经为您在脚本中创建,请修改固定参数重新运行")
    exit()
os.system("java -jar /ql/repo/zijiahong_bilibili/BILIBILI-HELPER.jar /ql/repo/zijiahong_bilibili/bilibili_config.json")
