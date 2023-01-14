from fastapi import Depends
from config.database import get_db

from models.usermodels import User
from sqlalchemy.orm import Session
from dto.userschema import RegisterUser
from config.hashing import Hashing


class UserService:
    def get_allUser(db: Session):
        return db.query(User).all()

    def get_user(useremail: str, db: Session):
        show_u = db.query(User).filter(User.email == useremail).first()
        

        response = {
            "id" : show_u.id,
            "name" : show_u.name,
            "email" : show_u.email,
            "mobile" : show_u.mobile,
            "is_active" : show_u.is_active,
        }
        return response

    def create_user(user: RegisterUser, db: Session = Depends(get_db)):
        db_user = User(
            name=user.name,
            email=user.email,
            password=Hashing.bcrypt(user.password),
            mobile=user.mobile,
            is_active=user.is_active,
        )

        db.add(db_user)
        db.commit()

        db.refresh(db_user)
        db_user.password = None

        return db_user
    

    def update_user(userid: int, user: RegisterUser, db: Session):
        db_userid = db.query(User).filter(User.id == userid).first()

        db_userid.name = user.name
        db_userid.email = user.email
        db_userid.password = Hashing.bcrypt(user.password)
        db_userid.mobile = user.mobile
        db_userid.is_active = user.is_active

        db.commit()

        return db_userid

    def deleteUser(userid: int, db: Session):
        db_userid = db.query(User).filter(User.id == userid).first()

        db.delete(db_userid)

        db.commit()

        return db_userid

