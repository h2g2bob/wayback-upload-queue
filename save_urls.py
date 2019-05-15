from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import quote_plus
from time import sleep
import sys

def save_url(driver, url):
    driver.get("https://web.archive.org/save/{}".format(url))
    for _ in range(12):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(10)
    driver.save_screenshot('screenshot-{}.png'.format(quote_plus(url)))

def main():
    # Maybe works:
    # driver = webdriver.PhantomJS(service_log_path="/tmp/wayb-pjs.log")
    # But there's no geckodriver debian package:
    # driver = webdriver.Firefox(service_log_path="/tmp/wayb-ff.log")
    # Works great, but needs a fake X11 buffer `Xvfb :99 -ac`
    driver = webdriver.Chrome(service_log_path="/tmp/wayb-ch.log")
    for url in sys.stdin:
        save_url(driver, url)
    driver.close()

if __name__ == '__main__':
    main()
