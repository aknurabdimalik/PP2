import psycopg2

def drop_tables():
    conn = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    password = "1234",
    host = "localhost"
    )
    cur = conn.cursor()
    
    cur.execute("DROP TABLE IF EXISTS Phonebook CASCADE;")
    
    conn.commit()
    cur.close()
    conn.close()
    print(" таблица удалена")
    
drop_tables()
    
    