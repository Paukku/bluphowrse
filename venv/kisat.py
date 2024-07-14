import time
import random


def trail(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[1]/td[3]/a").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
        sleep()
    except:
        input("Jokin meni pieleen? Mene hevosen sivulle")


def cutting(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[1]/td[2]/a").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
        sleep()
    except:
        driver.refresh()
        sleep()
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[1]/td[2]/a").click()
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
        sleep()

def wp(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[2]/td[3]/a").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
        sleep()
    except:
        driver.refresh()
        sleep()
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[2]/td[3]/a").click()
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
        sleep()
    
def tynnyri(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[1]/td[1]/a").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
        sleep()
    except:
        driver.refresh()
        sleep()
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[1]/td[1]/a").click()
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
        sleep()

def maasto(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[2]/td[1]/a").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
        sleep()
    except:
        input("Jokin meni pieleen? Mene hevosen sivulle")


def ravi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[1]/td[1]/a").click()
        sleep()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
        sleep()
        sleep()
    except:
        input("Jokin meni pieleen? Mene hevosen sivulle")


def sleep():
    time.sleep(random.uniform(0.56, 1.04))