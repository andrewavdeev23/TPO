from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s=Service('C:/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login")
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("andrew.avdeev23@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("Vaz2112gti")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

wait = WebDriverWait(driver, 30)
elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name")))

driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
driver.find_element(By.ID, "surname").send_keys("Лучшая")
driver.find_element(By.ID, "name").send_keys("Площадка")
driver.find_element(By.ID, "patronymic").send_keys("Бамблби")
driver.find_element(By.CSS_SELECTOR, "#birthday .mx-input").send_keys("01.01.1990")
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys(Keys.HOME)
driver.find_element(By.ID, "passportNumber").send_keys("666666")
driver.find_element(By.ID, "passportSeries").send_keys(Keys.HOME)
driver.find_element(By.ID, "passportSeries").send_keys("3333")
driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").send_keys("01.01.1992")
driver.find_element(By.ID, "code").send_keys(Keys.HOME)
driver.find_element(By.ID, "code").send_keys("666666")
driver.find_element(By.ID, "cardId").send_keys(Keys.HOME)
driver.find_element(By.ID, "cardId").send_keys("66666666666")
driver.find_element(By.ID, "issued").send_keys("кем-то")
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("Тюмень")

elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".vue-dadata__suggestions-item")))
elem.click()

driver.find_element(By.ID, "phone").send_keys(Keys.HOME)
driver.find_element(By.ID, "phone").send_keys("9999999994")
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys('C:\statement.pdf')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#скролим, потому что он не видит кнопки.

elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div[3]/div/div/div[2]/div[3]/div[9]/button[2]')))
elem.click()
