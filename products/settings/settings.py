from pathlib import Path

SERVICE_DIR = Path(__file__).resolve().parent.parent

DB_ROOT_PATH = Path(__file__).resolve().parent.parent.parent
DB_PATH = f'{DB_ROOT_PATH}/db.sqlite3'
