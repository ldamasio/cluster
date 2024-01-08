import psycopg2

conn = None

try:
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='Gze24+',
        host='upload.garagemdoze-lts.com',
        port='5432',
        # sslmode='require'
    )

    print("Success: Connected to the database!")
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("You are connected to - ", record, "\n")
    cur.close()

except (Exception, psycopg2.DatabaseError) as error:
    print("Error: ", error)

finally:
    if conn is not None:
        conn.close()
        print("Database connection closed.")