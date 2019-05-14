from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import quote_plus
import sys

def save_url(driver, url):
    driver.get("https://web.archive.org/save/{}".format(url))
    for _ in range(12):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(10)
    driver.save_screenshot('screenshot-{}.png'.format(quote_plus(url)))

def main():
    driver = webdriver.Firefox()
    for url in sys.stdin:
        save_url(driver, url)
    driver.close()

if __name__ == '__main__':
    main()
