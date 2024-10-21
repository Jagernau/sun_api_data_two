from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import config
import db_connect
from sqlalchemy.orm import Session

app = FastAPI()

# Задаем токен для проверки
fake_token = str(config.API_TOKEN)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()

# origins = [
#     "*",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

def get_db():
    session = db_connect.SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()



class ClientToken(BaseModel):
    client_token: str


# Функция для проверки токена
def verify_token(token: str = Depends(oauth2_scheme)):
    if token != fake_token:
        raise HTTPException(status_code=403, detail="Invalid token")

@app.get("/all_objects/")
async def get_all_objects(
        client_token: ClientToken,
        token: str = Depends(verify_token),
        db: Session = Depends(get_db)
        ):
    """ 
    Отдаёт все объекты
    """
    client_data = client_token.client_token
    try:
        resp = None
        return resp

    except:
        raise HTTPException(status_code=404, detail="File not found")
