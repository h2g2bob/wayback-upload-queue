import sqlite3
import sys
import logging

def main():
    with sqlite3.connect('queue.db') as conn:
        with conn: # transaction
            for url in sys.stdin:
                add_url(conn, url)

def add_url(conn, url):
    cur = conn.cursor()
    url = url.strip()
    if url == "":
        logging.warn("Ignoring empty line")
    elif not (url.startswith("http://") or url.startswith("https://")):
        logging.error("Line is not http:// or https:// -- %r", repr(url))
    else:
        logging.debug("Inserting %s", url)
        cur.execute("""
            INSERT OR IGNORE
            INTO queue (url, when_push)
            VALUES (?, CURRENT_TIMESTAMP);
        """, (url,))

if __name__ == '__main__':
    logging.basicConfig()
    main()
