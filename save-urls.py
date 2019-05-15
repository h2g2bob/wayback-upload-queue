from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import quote_plus
from time import sleep
import sqlite3
import logging

def get_driver():
    # Maybe works:
    # driver = webdriver.PhantomJS(service_log_path="/tmp/wayb-pjs.log")
    # But there's no geckodriver debian package:
    # driver = webdriver.Firefox(service_log_path="/tmp/wayb-ff.log")
    # Works great, but needs a fake X11 buffer `Xvfb :99 -ac`
    driver = webdriver.Chrome(service_log_path="/tmp/wayb-ch.log")
    return driver

def save_url(driver, url):
    driver.get("https://web.archive.org/save/{}".format(url))
    for _ in range(12):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(10)
    driver.save_screenshot('screenshot-{}.png'.format(quote_plus(url)))

def take_url(conn):
    cur = conn.cursor()
    try:
        cur.execute("BEGIN EXCLUSIVE TRANSACTION")
        cur.execute("SELECT url FROM queue WHERE when_push IS NULL")
        rows = cur.fetchall()
        if not rows:
            logging.info("No more work to do")
            return None
        [[url]] = rows
        cur.execute("UPDATE queue SET when_pop = CURRENT_TIMESTAMP WHERE url = ?", (url,))
        logging.info("Taken url %s", url)
        return url
    except Exception:
        cur.execute("ROLLBACK TRANSACTION")
        raise
    finally:
        cur.execute("COMMIT TRANSACTION")

def finished_url(conn, url):
    with conn: # transaction
        cur = conn.cursor()
        cur.execute("UPDATE queue SET when_finished = CURRENT_TIMESTAMP WHERE url = ?", (url,))

def main():
    driver = get_driver()
    with sqlite3.connect('queue.db') as conn:
        while True:
            url = take_url(conn)
            if url is None:
                break

            save_url(driver, url)

            finished_url(conn, url)

    driver.close()

if __name__ == '__main__':
    main()
