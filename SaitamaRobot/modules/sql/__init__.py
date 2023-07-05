from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

DB_URL = "postgres://erhftgpv:Q5hddUsSrBz1Q8pQTdsGLf3oe9eKdviu@lallah.db.elephantsql.com/erhftgpv"



def start() -> scoped_session:

    engine = create_engine(DB_URL, client_encoding="utf8")

    BASE.metadata.bind = engine

    BASE.metadata.create_all(engine)

    return scoped_session(sessionmaker(bind=engine, autoflush=True))





BASE = declarative_base()

SESSION = start()
