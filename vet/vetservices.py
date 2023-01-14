from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from config.database import get_db
from models.vetmodel import VetModel
from dto.vetschema import VetSchema

class VetService:
    def get_all_vet(db: Session):
        return db.query(VetModel).all()

    def create_vet(request: VetSchema, db: Session):
        new_vet = VetModel(
        name=request.name,
        gender=request.gender,
        phone=request.phone,
        email=request.email,
        degree=request.degree,
        address=request.address,
        clinic_name=request.clinic_name,
        registration_id=request.registration_id,
        opening_time=request.opening_time,
        closing_time=request.closing_time,
        )

        db.add(new_vet)
        db.commit()
        db.refresh(new_vet)

        return new_vet

    def show_vet(vetid: int, db: Session):
        show_p = db.query(VetModel).filter(VetModel.id == vetid).first()

        response = {
            "id": show_p.id,
            "name": show_p.name,
            "gender": show_p.gender,
            "phone": show_p.phone,
            "email": show_p.email,
            "degree": show_p.degree,
            "address": show_p.address,
            "clinic_name": show_p.clinic_name,
            "registration_id": show_p.registration_id,
            "opening_time": show_p.opening_time,
            "closing_time": show_p.closing_time,
        }

        return response

    def update_vet(vetid: int, request: VetModel, db: Session):
        vet_id = db.query(VetModel).filter(VetModel.id == vetid).first()
        
        vet_id.name = request.name
        vet_id.gender = request.gender
        vet_id.phone = request.phone
        vet_id.email = request.email
        vet_id.degree = request.degree
        vet_id.address = request.address
        vet_id.clinic_name = request.clinic_name
        vet_id.registration_id = request.registration_id
        vet_id.opening_time = request.opening_time
        vet_id.closing_time = request.closing_time

        return vet_id

    def delete_vet(vetid: int, db: Session):
        del_vet = (
            db.query(VetModel).filter(VetModel.id == vetid).first()
        )

        db.delete(del_vet)
        db.commit()

        return "Done"

