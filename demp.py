import markdown 
markdown_content="""
# 步骤

## 1.云服务器(ubuntu系统)安装chrome chromedriver

```shell
sudo apt-get install libxss1 libappindicator1 libindicator7 (apt-get error的话就apt-get update 或更新软件源)

 google-chrome --version
 
 wget https://chromedriver.storage.googleapis.com/xxxxx/chromedriver_linux64.zip  xxxx和google-chrome大致版本一致
 (https://chromedriver.chromium.org/downloads)
 
 unzip chromedriver_linux64.zip -d /usr/bin

 chromedriver --version
```

## 2.代码（没有selenium需要apt-get install selenium）

```python
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 无GUI
import time
import datetime
import os
# 设置全局变量
stuIDs = ["21"]

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
            dfs(stuID,1)
    driver.quit()


if __name__ == '__main__':
    tianbiao()
```

## 3.设置定时执行 上段代码

```python
# 启动cron
service cron start
# 编辑时间
crontab -e
5 0 * * *  python3 ~/fillin.py  # 每天的0:05分执行
```


"""
extensions = [
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.toc',
    'markdown.extensions.tables'
]
body_html = markdown.markdown(markdown_content, extensions=extensions)
file=open('./demo.txt','w')
file.write(body_html)
file.close()
