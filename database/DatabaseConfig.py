import os
from pathlib import Path
from dotenv import load_dotenv

current_dir = Path(__file__).parent
env_path = current_dir.parent / ".env"
load_dotenv(env_path)

PG_USER = os.getenv("PG_USER")
PG_PORT = os.getenv("PG_PORT")
PG_DBNAME = os.getenv("PG_DBNAME")
PG_PASSWORD = os.getenv("PG_PASSWORD")