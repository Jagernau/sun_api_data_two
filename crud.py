from sqlalchemy.orm import Session
from mysql_models import *


def get_from_pk(db: Session):
    return db.query(CaObject).all()
