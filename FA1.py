"""
TSS log generation, debug of the turret specified
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\webdrivers\chrome\chromedriver.exe")

driver.get("http://10.221.6.162/IptradeNet/Login.aspx?ReturnUrl=%2fiptradenet%2f")

driver.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_LoginButton']").click()
driver.find_element(By.XPATH,"//body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/table[3]/tbody[1]/tr[6]/td[1]/div[1]/table[1]/tbody[1]/tr[4]/td[2]/a[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_loginForm_UserName']").send_keys("admin1")
driver.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_loginForm_Password']").send_keys("admin1")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_loginForm_LoginButton']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='div_system']").click()   #system
time.sleep(2)
driver.find_element(By.XPATH,"//td[normalize-space()='Sessions']").click()    #session
time.sleep(2)

driver.find_element(By.XPATH,"//div[@id='sessions0_sdiv']").click()

time.sleep(2)

class DemoPrint():
    def printdetails(self):

        device_Identifier= driver.find_element(By.XPATH,"//a[normalize-space()='00-18-7D-B9-62-F3']").text
        print(device_Identifier)
    def Reboot(self):
        driver.find_element(By.ID,"ContentPlaceHolder1_UCTerminalSessionsList1_dataList_btnMore_1").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//label[@for='ContentPlaceHolder1_UCTerminalSessionsList1_actionReboot']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_UCTerminalSessionsList1_btnApplyAction']").click()
    def Remotelogin(self):
        driver.find_element(By.ID,"ContentPlaceHolder1_UCTerminalSessionsList1_dataList_btnMore_1").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//label[@for='ContentPlaceHolder1_UCTerminalSessionsList1_actionRemoteLogin']").click()
        time.sleep(5)
        driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$UCTerminalSessionsList1$tbUserLogin").send_keys("Jainendra")
        driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$UCTerminalSessionsList1$btnSearchUsers").click()
        time.sleep(7)
        driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$UCTerminalSessionsList1$btnApplyAction").click()
        time.sleep(2)
    def GenDump(self):
        driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$UCTerminalSessionsList1$dataList$ctl02$btnDump").click()
        time.sleep(2)
        driver.find_element(By.ID, "div_system").click()  # system
        time.sleep(2)
        driver.find_element(By.ID, "system0_div").click()  # system0_div -> monitor 1 ->provision 2->sessions....
        time.sleep(2)
        driver.find_element(By.ID,"monitoring1_sdiv").click()
        time.sleep(5)
        driver.find_element(By.ID,"ContentPlaceHolder1_UCDebugInfoList1_dataList_lnEdit_1").click()
        time.sleep(5)
    def TssLog(self):
        driver.find_element(By.ID, "div_system").click()  # system
        time.sleep(2)
        driver.find_element(By.ID, "system0_div").click()  # system0_div -> monitor 1 ->provision 2->sessions....
        time.sleep(2)
        driver.find_element(By.ID, "monitoring3_sdiv").click()
        time.sleep(5)
        driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bRefresh").click()
        time.sleep(5)
        driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$bDownload").click()
        time.sleep(5)
    def cluster_Tpo_monitor(self):
        driver.find_element(By.ID,"div_device_management").click()
        driver.find_element(By.ID,"device_management7_sdiv").click()
        # aTagsInLi = driver.find_elements_by_css_selector('li a')
        # # for a in aTagsInLi:
        # #     print (a.get_attribute('href'))
        driver.find_element(By.CSS_SELECTOR,"#ContentPlaceHolder1_ucTpoProfilesList_dataList_hyperLinkProfileEdition_0").click()
        driver.find_element(By.XPATH,"") #//div[@id='body-ctn']//table//tr//td//table//table//td//table//tr//td[@xpath="9"]
        # driver.find_element()
dp=DemoPrint()
# dp.printdetails()
# dp.Reboot()
# dp.Remotelogin()
# dp.GenDump()
dp.TssLog()
# dp.cluster_Tpo_monitor()