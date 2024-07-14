import time
import random
import selenium


def sleep():
    time.sleep(random.uniform(0.28, 0.40))

def puolituntia(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[2]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 0.5 h")

def tunti(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[3]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 1 h")

def puolitoista(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[4]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 1.5 h")

def kaksi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 2 h")

def kaksipuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[6]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 3 h")

def kolme(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[7]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 3.5 h")

def kolmepuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[8]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 4 h")

def nelja(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[9]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 4.5 h")

def neljapuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[10]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 5 h")

def viisi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[11]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 0.5 h")

def viisipuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[12]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 5.5 h")

def kuusi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[13]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 6 h")

def kuusipuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[14]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 6.5 h")

def seitseman(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[15]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 7h")

def seitsemanpuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[16]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 7.5 h")

def kahdeksan(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[17]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 8 h")

def kahdeksanpuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[18]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Este 8.5 h")