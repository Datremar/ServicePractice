from sqlalchemy.orm import sessionmaker

from database.engine import engine

_sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():
    return _sessionmaker
