class PostgresDb:
    async def connect():
        pass

db_connection = PostgresDb()
async def init_database() -> None:
    await db_connection.connect