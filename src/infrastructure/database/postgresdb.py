from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from pydantic import BaseModel
from urllib.parse import quote_plus
from ...core.config import get_settings
settings = get_settings()

password = quote_plus(settings.postgres_config.password)
DB_URL = f"postgresql+psycopg2://{settings.postgres_config.username}:{password}@{settings.postgres_config.host}:{settings.postgres_config.port}/{settings.postgres_config.database}"
engine = create_engine(DB_URL, echo=False)
db_session = sessionmaker(bind=engine, autoflush=False)


async def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close

async def check_database() -> None:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("DB connected")
        return    
    except Exception as e:
        print(f"Unable to connect to POSTGRESDB")
        raise e        

