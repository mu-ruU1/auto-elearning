#
#
#はじめにお読みください 
#
#(1) コマンドプロンプトにてpipのアップデート　> pip install --upgrade pip
#
#(2) WindowsマシンにPythonをインストール　https://www.python.jp/install/windows/install.html
#
#(3) selenium Pythonのインストール　> pip install selenium
#
#(4) ChromeDriverのインストール　https://www.seleniumqref.com//introduction/java/Java_Dl2.html
#
#

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.chrome.options import Options
import time
import library

options = Options()


#chromeのウィンドウを非表示にしてバックグラウンドで処理する場合、下のオプションをアンコメント
# options.add_argument('--headless') 
options.add_argument('--use-fake-ui-for-media-stream')
options.add_argument('--user-fake-device-for-media-stream')

CHROMEDRIVER = library.chromedriver

driver = webdriver.Chrome(CHROMEDRIVER,options=options)
driver.set_page_load_timeout(5)

driver.get(library.URL)

ID = driver.find_element_by_id("AccountId")
PW = driver.find_element_by_id("Password")

#idとpwの入力
ID.send_keys(library.myid)
PW.send_keys(library.mypw)

clicklogin = driver.find_element_by_id("BtnLogin")
clicklogin.click()

clickcourse = driver.find_element_by_id("LbtSubCourseLink_0")
clickcourse.click()

time.sleep(1)

clicksubcourse = driver.find_element_by_xpath('//*[@id="DivAllSubCourseTable"]/table/tbody/tr/td[2]/table/tbody/tr[3]/td[1]/a')
clicksubcourse.click()

time.sleep(1)

# ～～～ループ～～～～～～～～～～～～～～～～～～～～～～～～～～
for i in range(library.trynum):
    
    clicktype = driver.find_element_by_xpath('//*[@id="nan-contents"]/div[7]/div/table/tbody/tr[43]/td[1]/a')
    clicktype.click()

    time.sleep(2)
    
    # ウィンドウハンドルを取得する(list型配列)
    handle_array = driver.window_handles

    # seleniumで操作可能なdriverを切り替える
    driver.switch_to.window(handle_array[1])

    time.sleep(1)

    clickstart = driver.find_element_by_xpath('//*[@id="nan-contents-cover-buttons"]/div/div[1]/button')
    clickstart.click()

    time.sleep(3)

    clickok = driver.find_element_by_xpath('/html/body/div[13]/div[3]/div/button/span')
    clickok.click()

    for i in range(4):

        clickq1 = driver.find_element_by_xpath('//*[@id="0"]')
        clickq1.click()

        clicka1 = driver.find_element_by_xpath('//*[@id="nan-toolbox-content"]/div[2]/div[1]/button[1]/span')
        clicka1.click()

        clickn1 = driver.find_element_by_xpath('//*[@id="nan-toolbox-content"]/div[2]/div[1]/button[2]/span[1]')
        clickn1.click()

    clickq1 = driver.find_element_by_xpath('//*[@id="0"]')
    clickq1.click()

    clicka1 = driver.find_element_by_xpath('//*[@id="nan-toolbox-content"]/div[2]/div[1]/button[1]/span')
    clicka1.click()

    clicknext = driver.find_element_by_xpath('//*[@id="nan-toolbox-footer"]/button/span[1]')
    clicknext.click()

    time.sleep(3)

    clickokk = driver.find_element_by_xpath('/html/body/div[13]/div[3]/div/button/span')
    clickokk.click()

    time.sleep(1)

    clickbatu = driver.find_element_by_xpath('//*[@id="nan-mainframe-header-tools-quit"]')
    clickbatu.click()

    time.sleep(1)

    clickend = driver.find_element_by_xpath('/html/body/div[13]/div[3]/div/button[1]/span')
    clickend.click()

    time.sleep(3)

    driver.switch_to.window(handle_array[0])

    time.sleep(1)

driver.close()
print("正常に完了しました")

time.sleep(1)

print("終了します.....")

time.sleep(2)

driver.quit()