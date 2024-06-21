import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

doneMsg ="""

██████╗░░█████╗░███╗░░██╗███████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝
██║░░██║██║░░██║██╔██╗██║█████╗░░
██║░░██║██║░░██║██║╚████║██╔══╝░░
██████╔╝╚█████╔╝██║░╚███║███████╗
╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝"""

extractedMsg ="""

▒█▀▀▀ ▀▄▒▄▀ ▀▀█▀▀ ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀▄ 
▒█▀▀▀ ░▒█░░ ░▒█░░ ▒█▄▄▀ ▒█▄▄█ ▒█░░░ ░▒█░░ ▒█▀▀▀ ▒█░▒█ 
▒█▄▄▄ ▄▀▒▀▄ ░▒█░░ ▒█░▒█ ▒█░▒█ ▒█▄▄█ ░▒█░░ ▒█▄▄▄ ▒█▄▄▀"""

headStat = input("If you don't want to see Chrome during operation, type N:\n")

option = Options()
if(headStat.upper() == "N"):
    print("When you are using Chrome's headless mode, there might be some errors on debug console. Just, don't care. Everthing ok.")
    #time.sleep(5)
    option.add_argument("--headless")

URL = "https://ais.osym.gov.tr/Yetki/Giris"

driver = webdriver.Chrome(options=option)
wait = WebDriverWait(driver, 15)


def waitTill(by, value, handle=None):
    try:
        wait.until(lambda d : findElement(by, value).is_displayed )
    except :
        if(handle == None):
            pass
        else:
            handle()


def findElement(by, value):
    return driver.find_element(by=by, value=value)

def sendKeyByName(textFieldName, data):
    field = findElement(By.NAME, textFieldName)
    field.clear()
    field.send_keys(data)

def loginPage():
    driver.get(URL)
    waitTill(By.ID, "btnSubmitLogin")
    sendKeyByName("TcKimlikNo", "TC") # ----------> TC = TC KİMLİK NO BURAYA
    sendKeyByName("Sifre", "OSYM-AIS-SIFRE") # -----> OSYM-AIS-SIFRE = ŞİFRE BURAYA (ÖSYM - AİS ŞİFRESİ OLMALI. EDEVLET DESTEĞİ YOK.)
    button = findElement(By.ID, "btnSubmitLogin")
    button.click()

def extractPage(page):
    with open("result.html", "w", encoding="utf-8") as f:
        f.write("")
        f.write(page)
        f.close()
        print(extractedMsg)

def invalidCreditError():
    raise ValueError("TC No veya Şifre Yanlış Girilmiş Olabilir")
        
loginPage()
resp = driver.get("https://ais.osym.gov.tr/Sonuc/Listele")
waitTill(By.LINK_TEXT, "Görüntüle", invalidCreditError)

while(len(driver.find_elements(by = By.LINK_TEXT, value = "Görüntüle"))<2):
    waitTill(By.CLASS_NAME, "non-existing-class")
    #time.sleep(3) -> can be used instead of waitTill, not recommended. 
    driver.refresh()
    print(driver.session_id)
    waitTill(By.LINK_TEXT,"Görüntüle")

assert len(driver.window_handles) == 1

findElement(By.LINK_TEXT, "Görüntüle").click()    

wait.until(EC.number_of_windows_to_be(2))

for window_page in driver.window_handles:
    if(window_page != driver.current_window_handle):
        driver.switch_to.window(window_page)

waitTill(By.CLASS_NAME, "table2x")

extractPage(driver.page_source)

print(doneMsg)

input()
