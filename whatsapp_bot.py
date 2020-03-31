from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Criei um bot pra mandar mensagem" # Mensagem a ser enviada aqui
        self.grupos = ["teste"] # Nome do grupo ou pessoa aqui
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def SendMensage(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)

        while True:
            for grupo in self.grupos:
                grupos =self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
                time.sleep(1)
                grupos.click()
                chat_box = self.driver.find_element_by_class_name('_1Plpp')
                time.sleep(1)
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                send = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(1)
                send.click()
                time.sleep(1)


bot = WhatsappBot()
bot.SendMensage()