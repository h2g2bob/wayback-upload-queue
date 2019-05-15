import sqlite3

def main():
    conn = sqlite3.connect('queue.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS queue (
            url TEXT PRIMARY KEY,
            when_push TEXT,
            when_pop TEXT,
            when_finished TEXT
        );
    """)

if __name__ == '__main__':
    main()
