import sqlite3


DATABASE_NAME = "birthday.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            current_gift INTEGER DEFAULT 1
        )
    """)

    connection.commit()
    connection.close()


def create_user(user_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, current_gift)
        VALUES (?, 1)
    """, (user_id,))

    connection.commit()
    connection.close()


def get_current_gift(user_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT current_gift
        FROM users
        WHERE user_id = ?
    """, (user_id,))

    result = cursor.fetchone()

    connection.close()

    if result is None:
        return 1

    return result[0]


def set_current_gift(user_id, gift_number):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET current_gift = ?
        WHERE user_id = ?
    """, (gift_number, user_id))

    connection.commit()
    connection.close()