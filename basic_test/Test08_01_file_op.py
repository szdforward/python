#coding=utf-8

"""
文件的操作 找到文件中匹配的那一行
"""
def funRe(line,tbl):
    matchObj  = re.match('.*"product":"(.*?)"'+'.*'+tbl+'.*',line)
    if matchObj:
        print(matchObj.group(1) + '\t' + tbl)
        return True
    else:
        return False
import os
import re
# files = os.listdir("F:\python_resources\day37-python\day37课件资料")
# logfile=[f for f in files if f.endswith('.exe') ]
# print(logfile) # ['Anaconda3-2.4.1-Windows-x86_64.exe', 'pycharm-community-5.0.2.exe', 'python-3.8.2.exe', 'python-3.8.5-amd64.exe']
list = ["deskdict", "dict_banner", "dict_comment_server", "dict_community_server", "dict_listening", "dict_markets", "dict_push_server", "dict_suggest_server", "dictblog", "dictinfoline", "dictinfoline_recommendid", "dictmessage", "dictprofile", "dictsearch", "dictsearch_dict_noecceresult", "dictsearch_q", "dictweb_pageview_aged", "dictwordbook", "dict_app_embedded_wap", "dict_app_embedded_wap_paidu", "dict_app_embedded_wap_pen_linkage", "dict_baike_server", "dict_community", "dict_data_server", "dict_search_server", "dict_server", "dict_sign", "dict_usertask_server", "dict_vip", "dict_voice", "dict_yiju", "kid_dict_server", "kid_dict_server_all", "kiddict_market", "linuxdict", "mobile_mobile_dict_nps", "mobiledictclient_android_bg", "mobiledictclient_ipad", "mobiledictclient_perf", "mobiledictindexdetail", "mobiledictlocation_android", "mobiledictlocation_iphonepro", "picdictserver", "ugc_dict"]
fileHandler = open('F:/temp/dso.txt', 'a+')	#以读写方式处理文件IO 文件路径需要使用反斜杠
fileHandler.seek(0)
# # 读取一行
line = fileHandler.readline()
while line:
    # print(line)
    for tbl in list:
        if(funRe(line,tbl)):
            break
    line = fileHandler.readline()
fileHandler.close







