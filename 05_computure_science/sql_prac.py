import sqlite3

# 메모리 기반 SQLite 데이터베이스에 연결
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# 사람 정보를 저장할 테이블 생성
cursor.execute("""
CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# 몇 개의 데이터 삽입
cursor.executemany("INSERT INTO person (name, age) VALUES (?, ?)", [
    ('Alice', 25),
    ('Bob', 30),
    ('Charlie', 22),
    ('David', 28),
    ('Eva', 20)
])

conn.commit()
print("Table created and data inserted.")