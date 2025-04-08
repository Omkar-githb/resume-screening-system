import sqlite3

def init_db():
    conn = sqlite3.connect('resumes.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            resume_text TEXT,
            score REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_candidate(name, email, resume_text, score):
    conn = sqlite3.connect('resumes.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO candidates (name, email, resume_text, score)
        VALUES (?, ?, ?, ?)
    ''', (name, email, resume_text, score))
    conn.commit()
    conn.close()

def get_all_candidates():
    conn = sqlite3.connect('resumes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM candidates ORDER BY score DESC')
    data = c.fetchall()
    conn.close()
    return data
