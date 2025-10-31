from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

DB_URL = "postgresql+psycopg2://mohsinhassan:Mohsin%400421@localhost:5432/crm"
engine = create_engine(DB_URL, echo=True)
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

