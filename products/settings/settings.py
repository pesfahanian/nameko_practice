from pathlib import Path

DB_ROOT_PATH = Path(__file__).resolve().parent.parent.parent
DB_PATH = f'{DB_ROOT_PATH}/db.sqlite3'
