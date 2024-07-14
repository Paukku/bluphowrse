import time
import random
import selenium


def sleep():
    time.sleep(random.uniform(0.29, 0.41))

def puolituntia(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[2]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria puolituntia")

def tunti(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[3]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria tunti")


def puolitoista(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[4]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 1.5 tuntia")

def kaksi(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[5]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 2 tuntia")

def kaksipuoli(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[6]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 2.5 tuntia")

def kolme(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[7]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 3 tuntia")

def kolmepuoli(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[8]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 3.5 tuntia")

def nelja(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[9]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 4 tuntia")

def neljapuoli(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[10]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 4.5 tuntia")

def viisi(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[11]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 5 tuntia")

def viisipuoli(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[12]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 5.5 tuntia")

def kuusi(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[13]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 6 tuntia")

def kuusipuoli(driver):
    # Kouluttaa vuorta
    try:
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[14]")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
        klik.click()
        sleep()
    except:
        input("Vuoria 6.5 tuntia")
