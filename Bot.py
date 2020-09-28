import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Bot:

    def __init__(self, mail, con):
        self.driver = webdriver.Chrome("C:\chromedriver_win32/chromedriver.exe")
        self.mail = mail
        self.con = con
        self.login()
        print("Successful open")
        self.driver.minimize_window()

    def hide(self):
        self.driver.set_window_position(-2000, 0)

    def show(self):
        self.driver.maximize_window()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://csgofast.com/game/double")
        self.loginGoogle()

    def getcounter(self):
        try:
            counter = self.driver.find_element_by_xpath("//div[@class='inner']").text
            counter = int(counter)
        except:
            time.sleep(2)
            return self.getcounter()
        return counter

    # getacc returns the current balance of the account in cents
    def getacc(self):

        acc = self.driver.find_element_by_xpath("//div[@class='coins-component middle-block']").text
        while(acc == ''):
            acc = self.driver.find_element_by_class_name("//div[@class='coins-component middle-block']").text
        acc = acc[1:]
        return int(float(acc)*100)

    def loginGoogle(self):
        self.randwait(1)

        # busca el boton para iniciar sesion y aprieta
        signBtn = self.driver.find_elements_by_xpath("//button[@rv-on-click='view.login']")
        while len(signBtn) == 0:
            signBtn = self.driver.find_elements_by_xpath("//button[@rv-on-click='view.login']")
        signBtn[0].click()
        self.randwait(1)

        # busca el boton de google y aprieta
        try:
            googleBtn = self.driver.find_element_by_xpath("//button[@data-auth-provider='google']")
            googleBtn.click()
        except Exception as e:
            print(e)
            time.sleep(5)
            googleBtn = self.driver.find_element_by_xpath("//button[@data-auth-provider='google']")
            googleBtn.click()
        self.randwait(1)

        # cambia de pantalla a la de google
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

        #inserta el email
        mail = self.driver.find_elements_by_xpath("//input[@type='email']")
        while (len(mail)==0):
            mail = self.driver.find_elements_by_xpath("//input[@type='email']")
        mail[0].send_keys(self.mail)
        self.randwait()
        mail[0].send_keys(Keys.ENTER)  # manda el mail

        # inserta la contra
        self.randwait(2)
        contra = self.driver.find_elements_by_xpath("//input[@type='password']")
        while (len(contra) == 0):
            contra = self.driver.find_elements_by_xpath("//input[@type='password']")
        contra[0].send_keys(self.con)
        self.randwait()
        contra[0].send_keys(Keys.ENTER)  # manda la contra

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])  # vuelve a la pagina

        ##cierra el fucking popup
        self.randwait(1)
        try:
            bt = self.driver.find_element_by_id("onesignal-popover-cancel-button")
            bt.click()
        except:
            print("No pop up")
            self.randwait()

    def randwait(self, r=0):
        time.sleep(random.random() + r)



