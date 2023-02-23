import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 无GUI
import time
import datetime
import os
# 设置全局变量
stuIDs = ["211906354","211906308"]

# 如果检测到程序在 github actions 内运行，那么读取环境变量中的登录信息
if os.environ.get('GITHUB_RUN_ID', None):
    stuID = os.environ['stuID']

def tianbiao():
    chrome_options = Options()  # 无界面对象
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.add_argument('disable-dev-shm-usage')  # 禁用-开发-SHM-使用
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver)
    for stuID in stuIDs:
        try:
            # 表单地址
            url = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sjkrb.frm&op=h5&userno=' + stuID + '#/form'
            driver.get(url)  # 打开浏览器
            time.sleep(2)

            driver.maximize_window()  # 全屏
            time.sleep(4)

            # 滚动到底部
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 确认
            driver.find_element_by_xpath('//input[@type="checkbox"]').click()
            time.sleep(2)

            # 点击提交
            driver.find_element_by_xpath('//div[@id="SUBMIT"]').click()
            time.sleep(2)
            print(stuID + "打卡成功")

        except:
            FailLog.objects.create(status="fail",sno=stuID,time=datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S'))
            print(stuID + "打卡失败")
    driver.quit()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oj.settings')
    import django
    django.setup()
    from Backend.models.user.user import UserInfo
    for stu in UserInfo.objects.all():
        stuIDs.append(stu.sno)
        # stuIDs.append("211906354")
        tianbiao()
