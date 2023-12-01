from DB.DB import conn
import csv
def add_candidats(profile, name, location, salary, work_mode, stack, experience, resume, coment, hashtag):
    """Основная функция внесения клиентов в базу"""
    with conn.cursor() as cur:
        select_query = """INSERT INTO candidats(profile, name, location, salary, work_mode,
         stack, experience, resume, coment, hashtag) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cur.execute(select_query, (profile, name, location, salary, work_mode, stack, experience, resume, coment, hashtag))
        return 'Анкета добавлена'

def export_csv():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM candidats")
        result = cur.fetchall()
        with open('results.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(result)

export_csv()


