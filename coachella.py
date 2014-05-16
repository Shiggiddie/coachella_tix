from selenium import webdriver
#from random import randint #Necessary if you want to run test, below
from time import sleep

def main():
    try:
        driver = webdriver.Firefox()
    except:
        try:
            driver = webdriver.Chrome()
        except:
            print 'This only supports Firefox or Chrome, install one of those browsers and try again'
            return

    driver.get('https://coachella-weekend1.frontgatetickets.com/captcha.html')
    ps = driver.page_source
    driver.refresh()
    while ps == driver.page_source:
        print 'Page source did not change, refreshing in 0.5 seconds...'
        sleep(0.5)
        #A test I to see if this would actually work
        #if randint(0,20) >= 15:
        #    driver.get('www.google.com')
        #else:
        driver.refresh()

    print 'got out of the loop!'

if __name__ == '__main__':
    main()
