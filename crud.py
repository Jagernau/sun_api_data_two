from sqlalchemy.orm import Session
from mysql_models import *


def get_all_objects(db: Session):
    return db.query(CaObject).all()
