import os
from dotenv import load_dotenv
from pathlib import Path

env_path=Path('./.env')

load_dotenv(dotenv_path=env_path)

API_KEY=os.getenv('API_KEY')
SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM=os.getenv('ALGORITHM')