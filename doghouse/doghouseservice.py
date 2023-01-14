from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from config.database import get_db
from models.doghousemodel import DoghouseModel
from dto.doghouseschema import RegisterDoghouse

class DoghouseService:
    def get_all_doghouse(db: Session):
        return db.query(DoghouseModel).all()

    def create_doghouse(request: RegisterDoghouse, db: Session):
        new_doghouse = DoghouseModel(
        house_name=request.house_name,
        owner_name=request.owner_name,
        house_email=request.house_email,
        owner_email=request.owner_email,
        house_mobile=request.house_mobile,
        owner_mobile=request.owner_mobile,
        house_address=request.house_address,
        house_license=request.house_license,
        opening_time=request.opening_time,
        closing_time=request.closing_time,
        )

        db.add(new_doghouse)
        db.commit()
        db.refresh(new_doghouse)

        return new_doghouse

    def show_doghouse(doghouseid: int, db: Session):
        show_d = db.query(DoghouseModel).filter(DoghouseModel.id == doghouseid).first()

        response = {
            "id": show_d.id,
            "House Name": show_d.house_name,
            "Owner Name": show_d.owner_name,
            "House Email": show_d.house_email,
            "Owner Email": show_d.owner_email,
            "House Mobile": show_d.house_mobile,
            "Owner Mobile": show_d.owner_mobile,
            "House Address": show_d.house_address,
            "House License": show_d.house_license,
            "opening_time": show_d.opening_time,
            "closing_time": show_d.closing_time,
        }

        return response

    def update_doghouse(doghouseid: int, request: DoghouseModel, db: Session):
        doghouse_id = db.query(DoghouseModel).filter(DoghouseModel.id == doghouseid).first()
        
        doghouse_id.house_name = request.house_name
        doghouse_id.owner_name = request.owner_name
        doghouse_id.house_email = request.house_email
        doghouse_id.owner_email = request.owner_email
        doghouse_id.house_mobile = request.house_mobile
        doghouse_id.owner_mobile = request.owner_mobile
        doghouse_id.house_address = request.house_address
        doghouse_id.house_license = request.house_license
        doghouse_id.opening_time = request.opening_time
        doghouse_id.closing_time = request.closing_time

        return doghouse_id

    def delete_doghouse(doghouseid: int, db: Session):
        del_doghouse = (
            db.query(DoghouseModel).filter(DoghouseModel.id == doghouseid).first()
        )

        db.delete(del_doghouse)
        db.commit()

        return "Done"

