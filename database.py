import aiosqlite
import os

DATABASE_PATH = "database/aihub.db"


async def init_db():
    os.makedirs("database", exist_ok=True)

    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            is_admin INTEGER DEFAULT 0
        )
        """)
        await db.commit()


async def add_user(telegram_id, username, first_name, last_name):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("""
        INSERT OR IGNORE INTO users
        (telegram_id, username, first_name, last_name)
        VALUES (?, ?, ?, ?)
        """, (telegram_id, username, first_name, last_name))
        await db.commit()


async def get_user(telegram_id):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute(
            "SELECT * FROM users WHERE telegram_id = ?",
            (telegram_id,)
        )
        return await cursor.fetchone()


async def get_users_count():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("SELECT COUNT(*) FROM users")
        result = await cursor.fetchone()
        return result[0]