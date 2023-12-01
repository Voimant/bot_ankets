import psycopg2

with psycopg2.connect(user="voimant",
                      password='Alisvein11',
                      port='5432',
                      database='resume_db') as conn:
    def create_db():
        """ Создание таблицы в базе"""
        with conn.cursor() as cur:
            create_query = """ CREATE TABLE IF NOT EXISTS candidats(
            cand_id SERIAL PRIMARY KEY,
            profile VARCHAR(30) NOT NULL,
            name VARCHAR(30) NOT NULL,
            location VARCHAR(40) NOT NULL,
            salary TEXT NOT NULL,
            work_mode VARCHAR(30) NOT NULL,
            stack TEXT NOT NULL,
            experience TEXT NOT NULL,
            resume TEXT NOT NULL,
            coment TEXT NOT NULL,
            hashtag TEXT NOT NULL)"""
            cur.execute(create_query)
            return('Таблица создана')
    # print(create_db())
    # conn.commit()