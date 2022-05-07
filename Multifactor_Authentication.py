from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SeleniumExecutor:

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    def SetLoginAndClickNext(self, login):
        loginPage = 'file:///C:/Users/INY/oze-tech-assessment-QA/src/test/resources/__files/index.html'
        self.driver.get(loginPage)
        inputEmail = self.wait.until(EC.visibility_of_element_located((By.ID, "emailBox")))
        inputEmail.send_keys(login)
        Nextbutton = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="carouselExampleControls"]/div/div[1]/div/div[3]/a/button')))
        Nextbutton.click()

    def OpenCodePageAndReturnCode(self):
        codePage = 'file:///C:/Users/INY/oze-tech-assessment-QA/src/test/resources/__files/code.html'
        self.driver.get(codePage)
        code_Field = self.wait.until(EC.visibility_of_element_located((By.ID, "code")))
        code = code_Field.get_attribute("value")
        return code

    def SetCodeAndClickNext(self, code):
        self.SetLoginAndClickNext("test@devskiller.com")
        codeBox = self.wait.until(EC.visibility_of_element_located((By.ID, "codeBox")))
        codeBox.send_keys(code)
        nextButton = self.driver.find_element(By.CLASS_NAME, "buttonLoginCode")
        nextButton.click()
        time.sleep(2)


    def FillMaskedPasswordAndClickLogin(self, password):
        passwd = list(password)
        for p in passwd:
            count = 0
            passwdField = self.driver.find_elements(By.CLASS_NAME, "passwdField")

            for value in passwdField:
                if passwdField.is_enabled() == True:
                    value.click()
                    value.send_keys(p[count])
                else: pass
                count += 1

        logIn = self.driver.find_element(By.CSS_SELECTOR, "button[class=buttonLogin]")
        logIn.click()


    def GetLoggedInText(self):

        Text = self.driver.wait.until(EC.visibility_of_element_located((By.ID, "loggedIn"))).text
        return Text


SE = SeleniumExecutor()
SE.SetLoginAndClickNext("test@devskiller.com")
code = SE.OpenCodePageAndReturnCode()
SE.SetCodeAndClickNext(code)
SE.FillMaskedPasswordAndClickLogin("DevSkill1!")
SE.GetLoggedInText()



