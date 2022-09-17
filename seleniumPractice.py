from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get('https://codenboxautomationlab.com/registration-form/')
driver.maximize_window()
first_element = driver.find_element(By.ID, 'nf-field-17')
first_element.send_keys('Ajay')
last_element = driver.find_element(By.ID, 'nf-field-18')
last_element.send_keys('patil')
email_id = driver.find_element(By.ID, 'nf-field-19')
email_id.send_keys('ajay213@gmail.com')
phone_no = driver.find_element(By.ID, 'nf-field-20')
phone_no.send_keys('8888899999')

element = driver.find_element(By.ID, 'nf-field-22')
dropdown_ele = Select(element)

dropdown_ele.select_by_visible_text('Selenium Automation')

element2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/main/article/div/div[1]/div/div[4]/form/div/div[2]/nf-fields-wrap/nf-field[9]/div/div[2]/div/div[2]/select")
dropdown_ele2 = Select(element2)
# element2 = driver.find_element(By.XPATH, '//*[@id="nf-field-24"]')

dropdown_ele2.select_by_visible_text('May')
print(element2.text)

newsPaper = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/main/article/div/div[1]/div/div[4]/form/div/div[2]/nf-fields-wrap/nf-field[10]/div/div[2]/div/div[2]/ul/li[5]/label")
newsPaper.click()
print(newsPaper.text)


registerBTN = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/main/article/div/div[1]/div/div[4]/form/div/div[2]/nf-fields-wrap/nf-field[13]/div/div[2]/div/div[2]/input")
registerBTN.click()



