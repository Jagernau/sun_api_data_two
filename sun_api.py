from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import config
import db_connect
from sqlalchemy.orm import Session
import crud

app = FastAPI()

# Задаем токен для проверки
fake_token = str(config.API_TOKEN)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()


def get_db():
    session = db_connect.SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


# Функция для проверки токена
def verify_token(token: str = Depends(oauth2_scheme)):
    if token != fake_token:
        raise HTTPException(status_code=403, detail="Invalid token")

@app.get("/all_objects/")
async def get_all_objects(
        token: str = Depends(verify_token),
        db: Session = Depends(get_db)
        ):
    """ 
    Отдаёт все объекты
    """
    try:
        objects = crud.get_all_objects(db)
        if not objects:
            raise HTTPException(status_code=404, detail="Objects not found")
        return objects
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/detail_ok_obj_id/{obj_ok_id}")
async def get_object_detail(
    obj_ok_id: int,
    token: str = Depends(verify_token),
    db: Session = Depends(get_db)
):
    """
    Получение данных по конкретному объекту по его obj_ok_id
    """
    try:
        obj = crud.get_object_by_ok_id(db, obj_ok_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Object not found")
        return obj
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
