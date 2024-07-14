import time
import random
import selenium
from selenium import webdriver

import metsat
import vuoret
import koulu
import este
import ravi
import nopeus
import laukka
import kestavyys
import howrseblupfeed
import vuoretalleviisi
import rannat

import kisat

def log_in():
    driver = webdriver.Chrome('C:\\Users\\Paula\\Desktop\\howrsebot\\sele\\chromedriver')
    driver.get("http://wwww.howrse.fi")
    driver.maximize_window()
    sleep()
    driver.find_element_by_id('header-login-label').click()
    long_sleep()
    user = driver.find_element_by_id('login')

    sleep()

    sleep()
    driver.find_element_by_id('authentificationSubmit').click()
    sleep()

    # driver.get("https://www.howrse.fi/member/account/")
    # sleep()
    # driver.get("https://www.howrse.fi/member/account/?type=sharing")
    #
    # sleep()
    # # Menee esm. Esma = tr 1, Pizkunen tr 2
    # driver.find_element_by_xpath("html/body/div[@id='container']/main[@id='content']/section/section/div/div[@id='main-content']/div/article[2]/div/table/tbody/tr[3]/td[2]/button").click()
    # sleep()
    # long_sleep()

    driver.get("http://www.howrse.fi/elevage/chevaux/")
    long_sleep()

   # Blupattavan howrsen osoite tähän!
    driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=14435482')
    blup_knappe(driver)

def blup_knappe(driver):
    krs = 0
    while(krs < 10):
        sleep()

        round = 0
        metsatunnit = 6 # sama kuin round, laskee vaan kierrokset

        # Laskee tunnit
        koulutunnit = 0
        estetunnit = 0
        ravitunnit = 0
        laukkatunnit = 0
        nopeustunnit = 0
        maastotunnit = 0

        metsatunnit = varsa_aika(driver, metsatunnit)
        sleep()
        kouluta_metsat(driver, metsatunnit)
        sleep()


        # 2v ja 6kk
        hoida(driver)
        sleep()
        metsat.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        metsat.kaksi(driver)
        sleep()
        koulu.seitseman(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        koulu.kaksi(driver)
        sleep()

        age(driver)
        koulutunnit = koulutunnit + 11

        # kouluta koulu 8.5 ja 4.5 kolme kierrosta
        kouluta_koulu(driver, koulutunnit)

        # Ikä 3v 2kk, koulutetaan estettä
        sleep()
        hoida(driver)
        sleep()
        koulu.kaksipuoli(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        koulu.puoli(driver)
        sleep()
        este.kuusipuoli(driver)
        sleep()
        anna_herkut(driver)
        este.puolitoista(driver)
        sleep()
        age(driver)


        kouluta_este(driver, estetunnit)
        sleep()

        hoida(driver)
        sleep()
        este.kaksi(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        este.viisipuoli(driver)
        sleep()
        este.kaksi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        ravi.puolitoista(driver)
        sleep()
        age(driver)


        kouluta_ravi(driver, ravitunnit)
        sleep()

        hoida(driver)
        sleep()
        ravi.kaksi(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 10)
        sleep()
        ravi.kaksipuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        koulu.puoli(driver)
        sleep()
        age(driver)


        # Erikoistaminen länkkään
        driver.execute_script("window.scrollTo(0, 400)")
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div/div/div/div/div/div/ul/li[2]/span[3]/form/button").click()
        sleep()

        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div/div/div/div/a").click()
        sleep()
        sleep()
        # # Varusteiden laitto järjestys: lännensatulahuopa, lännensatula, lännensuitset
        driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div/div").click()
        sleep()

        driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/div/div[2]/div[3]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div[@id='choix-selle']/div").click()
        sleep()

        driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/div/div[2]/div[4]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div[@id='choix-bride']/div").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/button").click()
        sleep()

        # # Kisautus, 5 trail kisaa. Hepo 4v ja 10kk
        hoida(driver)
        sleep()
        driver.execute_script("window.scrollTo(0, 400)")
        sleep()
        kisat.trail(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 7)
        while(round < 4 ):
            sleep()
            kisat.trail(driver)
            round = round + 1

        sleep()
        anna_herkut(driver)
        sleep()

        # Erikoistaminen klassiseen
        try:
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-center']/div[2]/div/div/div[3]/div/div/button").click()
            sleep()
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-center']/div[2]/div/div/div[3]/div/div[2]/ul/li").click() # jos vaihtaa tuon li tähän: li[2] niin erikoistuu länteen
            sleep()
            driver.find_element_by_xpath("/html/body/div[@id='profil-popup']/span/div/form/table/tbody/tr[3]/td[2]/div[1]/input").click()
            sleep()
            driver.find_element_by_xpath("/html/body/div[@id='profil-popup']/span/div/form/div/button").click()
        except:
            driver.find_element_by_id(
                "horseNameRespecialisationClassique").click()
            sleep()
            driver.find_element_by_xpath("/html/body/div[@id='profil-popup']/span/div/form/div/button").click()

            pass
        sleep()
        age(driver)

        hoida(driver)
        sleep()
        nopeus.yksi(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 14)
        sleep()
        nopeus.viisi(driver)
        sleep()
        laukka.kaksi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        laukka.puolitoista(driver)
        sleep()
        age(driver)

        # kisauta ravia
        paivat = 0
        while(paivat < 3 ):
            hoida(driver)
            sleep()
            driver.execute_script("window.scrollTo(0, 400)")
            sleep()
            kisat.ravi(driver)
            sleep()
            howrseblupfeed.findfeed(driver, 8)
            round = 0
            while (round < 6):
                sleep()
                kisat.ravi(driver)
                round = round + 1

            sleep()
            anna_herkut(driver)
            sleep()
            age(driver)
            paivat = paivat + 1

        input("Onko kisautus ok?")
        # # # kisauta maastoa
        # #
        paivat = 0
        while (paivat < 3):
            hoida(driver)
            sleep()
            driver.execute_script("window.scrollTo(0, 400)")
            sleep()
            kisat.maasto(driver)
            sleep()
            howrseblupfeed.findfeed(driver, 7)
            round = 0
            while (round < 6):
                sleep()
                kisat.maasto(driver)
                round = round + 1

            sleep()
            anna_herkut(driver)
            sleep()
            age(driver)
            paivat = paivat + 1



        hoida(driver)
        vuoret.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        vuoret.neljapuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        vuoret.puolitoista(driver)
        sleep()
        age(driver)
        sleep()

        kouluta_vuoret(driver, vuoritunnit=0)
        # kouluta_rannat(driver, rantatunnit=0)

        # kouluta laukkaa
        kouluta_laukka(driver, laukkatunnit)
        # Kouluta nopeutta
        kouluta_nopeus(driver, nopeustunnit)

        # # # ikäännytä
        # more = 0
        # while(more < 4):
        #     hoida(driver)
        #     howrseblupfeed.findfeed(driver, 0)
        #     age(driver)
        #     more = more + 1


            #Heppa valmis 10v. ASTUTUKSET
        # MIETI MITEN TÄMÄ KANNATTAA TEHDÄ VIKSUSTI PUTKIA AJATELLEN?
        input("Astutukset.")
        

def blup_drum(driver):
    krs = 0
    while(krs < 10):
        sleep()

        round = 6
        metsatunnit = 6 # sama kuin round, laskee vaan kierrokset


        # # Laskee tunnit
        koulutunnit = 0
        estetunnit = 0
        ravitunnit = 0
        laukkatunnit = 0
        nopeustunnit = 0
        maastotunnit = 0
        #
        #
        #metsatunnit = varsa_aika(driver, metsatunnit)
        sleep()
        kouluta_metsat(driver, metsatunnit)
        sleep()


        # 2v ja 6kk
        hoida(driver)
        sleep()
        metsat.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        metsat.kaksi(driver)
        sleep()
        koulu.seitseman(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        koulu.kaksi(driver)
        sleep()

        age(driver)
        koulutunnit = koulutunnit + 11

        # kouluta koulu 8.5 ja 4.5 kolme kierrosta
        kouluta_koulu(driver, koulutunnit)

        # Ikä 3v 2kk, koulutetaan estettä
        sleep()
        hoida(driver)
        sleep()
        koulu.kaksipuoli(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        koulu.puoli(driver)
        sleep()
        laukka.kuusipuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        age(driver)


        kouluta_laukka(driver, estetunnit)
        sleep()

        hoida(driver)
        sleep()
        koulu.puoli(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 6)
        anna_herkut(driver)
        sleep()
        ravi.puolitoista(driver)
        sleep()
        age(driver)


        kouluta_ravi(driver, ravitunnit)
        sleep()

        hoida(driver)
        sleep()
        ravi.kaksi(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        ravi.kaksipuoli(driver)
        sleep()
        kestavyys.kolmepuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()

        # Erikoistaminen länkkään
        driver.execute_script("window.scrollTo(0, 400)")
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div/div/div/div/div/div/ul/li[2]/span[3]/form/button").click()
        sleep()

        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div/div/div/div/a").click()
        sleep()
        sleep()
        # # Varusteiden laitto järjestys: lännensatulahuopa, lännensatula, lännensuitset
        driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div/div").click()
        sleep()

        driver.find_element_by_xpath(
            "/html/body/div[@id='choisir-equipement-popup']/span/div/div/div[2]/div[3]").click()
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div[@id='choix-selle']/div").click()
        sleep()

        driver.find_element_by_xpath(
            "/html/body/div[@id='choisir-equipement-popup']/span/div/div/div[2]/div[4]").click()
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div[@id='choix-bride']/div").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/button").click()
        sleep()
        age(driver)
        sleep()

        # Kouluta kestävyys
        kouluta_kestavyys(driver, nopeustunnit)

        hoida(driver)
        sleep()
        kestavyys.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 14)
        sleep()
        kestavyys.viisi(driver)
        sleep()
        este.kaksi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        este.puolitoista(driver)
        sleep()
        age(driver)

        # # # Kisautus, 25 wp kisaa.
        # hoida(driver)
        # sleep()
        # driver.execute_script("window.scrollTo(0, 400)")
        # sleep()
        # kisat.wp(driver)
        # sleep()
        # howrseblupfeed.findfeed(driver, 7)
        # while (round < 4):
        #     sleep()
        #     kisat.wp(driver)
        #     round = round + 1
        #
        # sleep()
        # anna_herkut(driver)
        # sleep()
        # age(driver)
        #
        # # kisauta tynnyri
        # paivat = 0
        # while (paivat < 3):
        #     hoida(driver)
        #     sleep()
        #     driver.execute_script("window.scrollTo(0, 400)")
        #     sleep()
        #     kisat.tynnyri(driver)
        #     sleep()
        #     howrseblupfeed.findfeed(driver, 8)
        #     round = 0
        #     while (round < 6):
        #         sleep()
        #         kisat.tynnyri(driver)
        #         round = round + 1
        #
        #     sleep()
        #     anna_herkut(driver)
        #     sleep()
        #     age(driver)
        #     paivat = paivat + 1

        input("Onko kisautus ok?")

        hoida(driver)
        vuoret.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        vuoret.neljapuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        vuoret.puolitoista(driver)
        sleep()
        age(driver)
        sleep()

        kouluta_vuoret(driver, vuoritunnit=0)

        # kouluta laukkaa
        kouluta_este(driver, laukkatunnit)

        # # ikäännytä
        # moreage = 0
        # while(moreage < 4):
        #     hoida(driver)
        #     howrseblupfeed.findfeed(driver, 0)
        #     age(driver)

        #Heppa valmis 10v. ASTUTUKSET
        # MIETI MITEN TÄMÄ KANNATTAA TEHDÄ VIKSUSTI PUTKIA AJATELLEN?
        input("Astutukset.")


def blup_rollo(driver):
    krs = 0
    while (krs < 10):
        sleep()

        round = 6
        metsatunnit = 6  # sama kuin round, laskee vaan kierrokset

        # # Laskee tunnit
        koulutunnit = 0
        estetunnit = 0
        ravitunnit = 0
        laukkatunnit = 0
        nopeustunnit = 0
        maastotunnit = 0
        kestavyystunnit = 0
        # #
        # #
        # metsatunnit = varsa_aika(driver, metsatunnit)
        sleep()
        kouluta_rollo_vuoret(driver, metsatunnit)
        sleep()

        # 2v ja 6kk
        hoida(driver)
        sleep()
        vuoretalleviisi.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        vuoretalleviisi.kaksi(driver)
        sleep()
        koulu.seitseman(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        koulu.kaksi(driver)
        sleep()

        age(driver)
        koulutunnit = koulutunnit + 11

        # kouluta koulu 8.5 ja 4.5 kolme kierrosta
        kouluta_koulu(driver, koulutunnit)

        # Ikä 3v 2kk, koulutetaan estettä
        sleep()
        hoida(driver)
        sleep()
        koulu.kaksipuoli(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        koulu.puoli(driver)
        sleep()
        ravi.kuusi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        age(driver)

        kouluta_nopeus(driver, nopeustunnit)
        sleep()

        hoida(driver)
        sleep()
        koulu.puoli(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 6)
        anna_herkut(driver)
        sleep()
        nopeus.yksi(driver)
        sleep()
        age(driver)

        hoida(driver)
        sleep()
        nopeus.kaksi(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        nopeus.kaksipuoli(driver)
        sleep()
        kestavyys.kolmepuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()

        # Erikoistaminen länkkään
        driver.execute_script("window.scrollTo(0, 400)")
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div/div/div/div/div/div/ul/li[2]/span[3]/form/button").click()
        sleep()

        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div/div/div/div/a").click()
        sleep()
        sleep()
        # # Varusteiden laitto järjestys: lännensatulahuopa, lännensatula, lännensuitset
        driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div/div").click()
        sleep()

        driver.find_element_by_xpath(
            "/html/body/div[@id='choisir-equipement-popup']/span/div/div/div[2]/div[3]").click()
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div[@id='choix-selle']/div").click()
        sleep()

        driver.find_element_by_xpath(
            "/html/body/div[@id='choisir-equipement-popup']/span/div/div/div[2]/div[4]").click()
        sleep()
        driver.find_element_by_xpath(
            "/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div[@id='choix-bride']/div").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/button").click()
        sleep()
        age(driver)
        sleep()

        # Kouluta kestävyys
        kouluta_kestavyys(driver, kestavyystunnit)

        hoida(driver)
        sleep()
        kestavyys.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 14)
        sleep()
        kestavyys.viisi(driver)
        sleep()
        ravi.kaksi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        nopeus.yksi(driver)
        sleep()
        age(driver)

        # # Kisautus, 25 cutti kisaa.

        paivat = 0
        while (paivat < 4):
            hoida(driver)
            sleep()
            driver.execute_script("window.scrollTo(0, 400)")
            sleep()
            kisat.cutting(driver)
            sleep()
            howrseblupfeed.findfeed(driver, 8)
            round = 0
            while (round < 5):
                sleep()
                kisat.cutting(driver)
                round = round + 1

            sleep()
            anna_herkut(driver)
            sleep()
            age(driver)
            paivat = paivat + 1

        # kisauta reikku
        paivat = 0
        while (paivat < 3):
            hoida(driver)
            sleep()
            driver.execute_script("window.scrollTo(0, 400)")
            sleep()
            kisat.maasto(driver)
            sleep()
            howrseblupfeed.findfeed(driver, 8)
            round = 0
            while (round < 6):
                sleep()
                kisat.maasto(driver)
                round = round + 1

            sleep()
            anna_herkut(driver)
            sleep()
            age(driver)
            paivat = paivat + 1

        # input("Onko kisautus ok?")

        hoida(driver)
        metsat.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        metsat.neljajapuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        metsat.puolitoista(driver)
        sleep()
        age(driver)
        sleep()

        kouluta_rollo_metsa(driver, metsatunti=0)

        # kouluta laukkaa
        kouluta_ravi(driver, laukkatunnit)

        # # ikäännytä
        # moreage = 0
        # while(moreage < 4):
        #     hoida(driver)
        #     howrseblupfeed.findfeed(driver, 0)
        #     age(driver)

        # Heppa valmis 10v. ASTUTUKSET
        # MIETI MITEN TÄMÄ KANNATTAA TEHDÄ VIKSUSTI PUTKIA AJATELLEN?
        input("Astutukset.")

def blup_enkku(driver):
    krs = 0
    while (krs < 10):
        sleep()

        round = 0
        metsatunnit = 6  # sama kuin round, laskee vaan kierrokset

        # # Laskee tunnit
        koulutunnit = 0
        estetunnit = 0
        ravitunnit = 0
        laukkatunnit = 0
        nopeustunnit = 0
        maastotunnit = 0
        #
        #
        # # metsatunnit = varsa_aika(driver, metsatunnit)
        # sleep()
        # kouluta_metsat(driver, metsatunnit)
        # sleep()
        #
        # # 2v ja 6kk
        # hoida(driver)
        # sleep()
        # metsat.puolitoista(driver)
        # sleep()
        # howrseblupfeed.findfeed(driver, 15)
        # sleep()
        # metsat.kaksi(driver)
        # sleep()
        # koulu.seitseman(driver)
        # sleep()
        # anna_herkut(driver)
        # sleep()
        # koulu.kaksi(driver)
        # sleep()
        #
        # age(driver)
        # koulutunnit = koulutunnit + 11
        #
        # # kouluta koulu 8.5 ja 4.5 kolme kierrosta
        # kouluta_koulu(driver, koulutunnit)
        #
        # kouluta_laukka(driver, estetunnit)
        # sleep()
        #
        # hoida(driver)
        # sleep()
        # laukka.kaksi(driver)
        # sleep()
        # howrseblupfeed.findfeed(driver, 15)
        # sleep()
        # laukka.viisipuoli(driver)
        # sleep()
        # laukka.kaksi(driver)
        # sleep()
        # anna_herkut(driver)
        # sleep()
        # este.puolitoista(driver)
        # sleep()
        # age(driver)
        #
        # kouluta_nopeus(driver, nopeustunnit)
        # sleep()
        #
        # hoida(driver)
        # sleep()
        # # koulu.puoli(driver)
        # sleep()
        # howrseblupfeed.findfeed(driver, 6)
        # anna_herkut(driver)
        # sleep()
        # nopeus.yksi(driver)
        # sleep()
        # age(driver)
        #
        # hoida(driver)
        # sleep()
        # nopeus.kaksi(driver)
        # sleep()
        # howrseblupfeed.findfeed(driver, 15)
        # sleep()
        # nopeus.kaksipuoli(driver)
        # sleep()
        # este.kolmepuoli(driver)
        # sleep()
        # anna_herkut(driver)
        # sleep()
        #
        # # Erikoistaminen länkkään
        # driver.execute_script("window.scrollTo(0, 400)")
        # sleep()
        # driver.find_element_by_xpath(
        #     "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div/div/div/div/div/div/ul/li[2]/span[3]/form/button").click()
        # sleep()
        #
        # driver.find_element_by_xpath(
        #     "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div/div/div/div/a").click()
        # sleep()
        # sleep()
        # # # Varusteiden laitto järjestys: lännensatulahuopa, lännensatula, lännensuitset
        # driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div/div").click()
        # sleep()
        #
        # driver.find_element_by_xpath(
        #     "/html/body/div[@id='choisir-equipement-popup']/span/div/div/div[2]/div[3]").click()
        # sleep()
        # driver.find_element_by_xpath(
        #     "/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div[@id='choix-selle']/div").click()
        # sleep()
        #
        # driver.find_element_by_xpath(
        #     "/html/body/div[@id='choisir-equipement-popup']/span/div/div/div[2]/div[4]").click()
        # sleep()
        # driver.find_element_by_xpath(
        #     "/html/body/div[@id='choisir-equipement-popup']/span/div/div/form/div[@id='choix-bride']/div").click()
        # sleep()
        # driver.find_element_by_xpath("/html/body/div[@id='choisir-equipement-popup']/span/div/button").click()
        # sleep()
        #
        # # Erikoistaminen klassiseen
        # try:
        #     driver.find_element_by_xpath(
        #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-center']/div[2]/div/div/div[3]/div/div/button").click()
        #     sleep()
        #     driver.find_element_by_xpath(
        #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-center']/div[2]/div/div/div[3]/div/div[2]/ul/li").click()  # jos vaihtaa tuon li tähän: li[2] niin erikoistuu länteen
        #     sleep()
        #     driver.find_element_by_xpath(
        #         "/html/body/div[@id='profil-popup']/span/div/form/table/tbody/tr[3]/td[2]/div[1]/input").click()
        #     sleep()
        #     driver.find_element_by_xpath("/html/body/div[@id='profil-popup']/span/div/form/div/button").click()
        # except:
        #     input("Erikoista klassiseen ja paina enter")
        #     pass
        # sleep()

        # paivat = 0
        # while (paivat < 4):
        #     hoida(driver)
        #     sleep()
        #     driver.execute_script("window.scrollTo(0, 400)")
        #     sleep()
        #     kisat.cutting(driver)
        #     sleep()
        #     howrseblupfeed.findfeed(driver, 8)
        #     round = 0
        #     while (round < 5):
        #         sleep()
        #         kisat.cutting(driver)
        #         round = round + 1
        #
        #     sleep()
        #     anna_herkut(driver)
        #     sleep()
        #     age(driver)
        #     paivat = paivat + 1

        # kisauta maasto
        # paivat = 0
        # while (paivat < 3):
        #     hoida(driver)
        #     sleep()
        #     driver.execute_script("window.scrollTo(0, 400)")
        #     sleep()
        #     kisat.maasto(driver)
        #     sleep()
        #     howrseblupfeed.findfeed(driver, 8)
        #     round = 0
        #     while (round < 6):
        #         sleep()
        #         kisat.maasto(driver)
        #         round = round + 1
        #
        #     sleep()
        #     anna_herkut(driver)
        #     sleep()
        #     age(driver)
        #     paivat = paivat + 1

        input("Onko kisautus ok?")

        hoida(driver)
        vuoret.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        vuoret.neljapuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        vuoret.puolitoista(driver)
        sleep()
        age(driver)
        sleep()

        kouluta_vuoret(driver, vuoritunnit=0)

        input("Astutt")


def kouluta_rollo_vuoret(driver, vuoritunnit):

    # koulutus alkaa, vuoret eka. 1.5h, ruoki 12 kaura, 5h silitys, vesi, porkkana. 3 kierrosta
    while (vuoritunnit < 9):
        sleep()
        hoida(driver)
        sleep()
        vuoretalleviisi.alle2_puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 12)
        sleep()
        vuoretalleviisi.alle2_viisi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        vuoretalleviisi.alle2_puolitunti(driver)
        sleep()
        age(driver)
        sleep()
        vuoritunnit = vuoritunnit + 1

    # 2v kouluta metsiä, 1.5, 5,5 ja 1.5 3 kierrosta
    while (vuoritunnit < 12):
        sleep()
        hoida(driver)
        sleep()
        vuoretalleviisi.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        vuoretalleviisi.viisipuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        vuoretalleviisi.puolitoista(driver)
        sleep()
        age(driver)
        sleep()
        vuoritunnit = vuoritunnit + 1


def kouluta_rollo_metsa(driver, metsatunti):
    while (metsatunti < 95):
        hoida(driver)
        sleep()
        metsat.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        metsat.kuusi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        metsat.tunti(driver)
        sleep()
        age(driver)
        metsatunti = metsatunti + 8


def varsa_aika(driver, round):
    while (round < 6):
        sleep()
        hoida(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 0)
        sleep()
        age(driver)
        sleep()
        round = round + 1
    return round

def hoida(driver):
    #laita nukkumaan, hoida
    try:
        klik = driver.find_element_by_id("boutonPanser")
        klik.click()
        sleep()
    except:
        input("laita nukkumaan")
    try:
        klik = driver.find_element_by_id("boutonCoucher")
        klik.click()
        sleep()
    except:
        input("Hoida")

def anna_herkut(driver):
    # Silitys, vesi, porkkana, ape
    try:
        klik = driver.find_element_by_id("boutonCaresser")
        klik.click()
        sleep()
    except:
        input("Silitä")
    try:
        klik = driver.find_element_by_id("boutonBoire")
        klik.click()
        sleep()
    except:
        input("vesi")
    try:
        klik =driver.find_element_by_id("boutonCarotte")
        klik.click()
        sleep()
    except:
        input("porkkana")
    try:
        klik = driver.find_element_by_id("boutonMash")
        klik.click()
        sleep()
    except:
        input("ape")

def kouluta_metsat(driver, metsatunnit):

    # koulutus alkaa, metsät eka. 1.5h, ruoki 12 kaura, 5h silitys, vesi, porkkana. 3 kierrosta
    while (metsatunnit < 9):
        sleep()
        hoida(driver)
        sleep()
        metsat.alle2_puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 12)
        sleep()
        metsat.alle2_viisi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        metsat.alle2_puolitunti(driver)
        sleep()
        age(driver)
        sleep()
        metsatunnit = metsatunnit + 1

    # 2v kouluta metsiä, 1.5, 5,5 ja 1.5 3 kierrosta
    while (metsatunnit < 12):
        sleep()
        hoida(driver)
        sleep()
        metsat.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        metsat.viisijapuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        metsat.puolitoista(driver)
        sleep()
        age(driver)
        sleep()
        metsatunnit = metsatunnit + 1

def kouluta_koulu(driver, koulutunnit):

    while (koulutunnit < 50):
        hoida(driver)
        sleep()
        koulu.kahdeksanpuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 11)
        sleep()
        koulu.nelja(driver)
        sleep()
        age(driver)
        koulutunnit = koulutunnit + 13

def kouluta_este(driver, estetunnit):
    while (estetunnit < 32):
        hoida(driver)
        sleep()
        este.kaksi(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        este.seitsemanpuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        este.puolitoista(driver)
        sleep()
        age(driver)
        sleep()
        estetunnit = estetunnit +11

def kouluta_ravi(driver, ravitunnit):
    while (ravitunnit < 43):
        hoida(driver)
        sleep()
        ravi.kaksi(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        ravi.seitsemanpuoli(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        ravi.puolitoista(driver)
        sleep()
        age(driver)
        sleep()
        ravitunnit = ravitunnit +11

def kouluta_laukka(driver, laukkatunnit):
    while (laukkatunnit < 43):
        hoida(driver)
        sleep()
        laukka.kaksi(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 13)
        sleep()
        laukka.seitseman(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        laukka.puolitoista(driver)
        sleep()
        age(driver)
        laukkatunnit = laukkatunnit +11

def kouluta_nopeus(driver, nopeustunnit):
    while (nopeustunnit < 35):
        hoida(driver)
        sleep()
        nopeus.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        nopeus.kuusi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        nopeus.puolitoista(driver)
        sleep()
        age(driver)
        nopeustunnit = nopeustunnit + 9
        
def kouluta_kestavyys(driver, nopeustunnit):
    while (nopeustunnit < 35):
        hoida(driver)
        sleep()
        kestavyys.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        kestavyys.kuusi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        kestavyys.puolitoista(driver)
        sleep()
        age(driver)
        nopeustunnit = nopeustunnit + 9

def kouluta_vuoret(driver, vuoritunnit):
    while (vuoritunnit < 95):
        hoida(driver)
        sleep()
        vuoret.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        vuoret.kuusi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        vuoret.tunti(driver)
        sleep()
        age(driver)
        vuoritunnit = vuoritunnit + 8


def kouluta_rannat(driver, rantatunnit):
    while (rantatunnit < 80):
        hoida(driver)
        sleep()
        rannat.puolitoista(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 15)
        sleep()
        rannat.kuusi(driver)
        sleep()
        anna_herkut(driver)
        sleep()
        rannat.tunti(driver)
        sleep()
        age(driver)
        rantatunnit = rantatunnit + 8


def astuta_tamma(driver):
    driver.execute_script("window.scrollTo(0, 1090)")
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[5]/div/div/div/div/div/div/table/tbody/tr/td[3]/a").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='resultatsRecherche']/ul/li[2]/div/a").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='resultatsRecherche']/table/tbody/tr/td[8]/a").click()
    sleep()

    # astutus valittu, nyt astutukseen
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/button").click()
    sleep()


def sleep():
    time.sleep(random.uniform(1.57, 1.19))

def long_sleep():
    time.sleep(random.uniform(3.87, 4.09))


def age(driver):
    try:
        klik = driver.find_element_by_id("boutonVieillir")
        klik.click()
        sleep()
        klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]/div[2]/div[@id='night-body-content']/div[@id='night-wrapper']/div[@id='night-tab-age']/table/tbody/tr[2]/td/form/div/button")
        klik.click()
        sleep()
        sleep()
    except:
        input("Ei ikäänny")



if __name__ == "__main__":
    log_in()
    time.sleep(450)
    exit()