import time
import random
import selenium


def sleep():
    time.sleep(random.uniform(0.28, 0.41))


def puoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[2]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 0.5 tuntia")


def yksi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[3]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 0.5 tuntia")

def puolitoista(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[4]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 1 tuntia")

def kaksi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 1.5 tuntia")

def viisipuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[6]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 2 tuntia")

def kaksipuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[7]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 2.5 tuntia")

def kolme(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[8]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 3 tuntia")

def kolmepuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[9]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 3.5 tuntia")

def nelja(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[10]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 4 tuntia")

def neljapuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[11]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 4.5 tuntia")

def viisi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[12]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 5 tuntia")

def viisipuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[13]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 5.5 tuntia")

def kuusi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[14]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 6 tuntia")

def kuusipuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[15]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 6.5 tuntia")

def seitseman(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[16]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 07 tuntia")

def seitsemanpuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[17]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 7.5 tuntia")

def kahdeksan(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[18]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 8 tuntia")

def kahdeksanpuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[19]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 8.5 tuntia")

def yhdeksan(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[20]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 9 tuntia")

def yhdeksanpuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[21]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Laukka 9.5 tuntia")