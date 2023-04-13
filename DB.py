import psycopg2
from config import config

class DB:
    def __init__(self):
        self.params = config()
    
    def insert(self, thread, table):
        conn = None
        conn = psycopg2.connect(**self.params)
        conn.autocommit = True
        cur = conn.cursor()
        for post in thread.keys():
            time = thread[post]['time']
            for coin in thread[post]['coins']:
                query = '''INSERT INTO %s(number, time, coin) VALUES(%s, %s, '%s')''' % (table, post, time, coin)
                try:
                    cur.execute(query)
                    print("Success!")
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
        if conn is not None:
            conn.close()