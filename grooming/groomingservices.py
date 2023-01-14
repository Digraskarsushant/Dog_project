from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from config.database import get_db
from models.groomingmodel import GroomingModel
from dto.groomingschema import groomingschema



class GroomingService:
    def get_all_grooming(db: Session):
        return db.query(GroomingModel).all()

    def create_grooming(request: groomingschema, db: Session):
        new_grooming = GroomingModel(
            name=request.name,
            provider_name=request.provider_name,
            storename=request.storename,
            phone=request.phone,
            address=request.address,
            regestration_no=request.regestration_no,            
            opentime=request.opentime,
            closetime=request.closetime,
        )

        db.add(new_grooming)
        db.commit()
        db.refresh(new_grooming)

        return new_grooming

    def show_grooming(groomingid: int, db: Session):
        show_g = db.query(GroomingModel).filter(GroomingModel.id == groomingid).first()
        

        response = {
            "name": show_g.name,
            "provider_name": show_g.provider_name,
            "storename": show_g.storename,
            "phone": show_g.phone,
            "address": show_g.address,
            "opentime": show_g.opentime,
            "closetime": show_g.closetime,
            "regestration_no": show_g.regestration_no, 
        }

        return response

    # Lanjutlagi
    def update_grooming(groomingid: int, request: groomingschema, db: Session):
        grooming_id = db.query(GroomingModel).filter(GroomingModel.id == groomingid).first()

        grooming_id.name = request.name
        grooming_id.provider_name = request.provider_name
        grooming_id.storename = request.storename
        grooming_id.phone = request.phone
        grooming_id.address = request.address
        grooming_id.regestration_no = request.regestration_no
        grooming_id.opentime = request.opentime
        grooming_id.closetime = request.closetime
        db.commit()

        return grooming_id

    def delete_grooming(groomingid: int, db: Session):
        del_grooming = (
            db.query(GroomingModel).filter(GroomingModel.id == groomingid).first()
        )

        db.delete(del_grooming)
        db.commit()

        return "Done"

