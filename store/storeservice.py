from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from config.database import get_db
from models.storemodel import StoreModel
from dto.storeschema import StoreBase
from config.hashing import Hashing


class StoreService:
    def get_all_store(db: Session):
        return db.query(StoreModel).all()

    def create_store(request: StoreBase, db: Session):
        new_store = StoreModel(
            name=request.name,
            city = request.city,
            country = request.country,
            currency = request.currency,
            domain = request.domain,
            phone = request.phone,
            zipcode = request.zipcode,
            street = request.street,
            email = request.email
        )

        db.add(new_store)
        db.commit()
        db.refresh(new_store)

        return new_store

    def show_store(storeid: int, db: Session):
        show_s = db.query(StoreModel).filter(StoreModel.id == storeid).first()
        
        response = {
            "id" : show_s.id,
            "name" : show_s.name,
            "city" : show_s.city,
            "country" : show_s.country,
            "currency" : show_s.currency,
            "zipcode" : show_s.zipcode,
            "street" : show_s.street,
        }

        return response

    # Lanjutlagi
    def update_service(storeid: int, request: StoreBase, db: Session):
        store_id = db.query(StoreModel).filter(StoreModel.id == storeid).first()

        store_id.name = request.name
        store_id.city = request.city
        store_id.country = request.country
        store_id.currency = request.currency
        store_id.zipcode = request.zipcode
        store_id.street = request.street
        db.commit()

        return store_id

    def delete_service(storeid: int, db: Session):
        del_store = (
            db.query(StoreModel).filter(StoreModel.id == storeid).first()
        )

        db.delete(del_store)
        db.commit()

        return "Done"

