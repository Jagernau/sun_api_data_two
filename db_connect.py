
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config



engine = create_engine(str(config.connection_mysql))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


BASE = declarative_base()
