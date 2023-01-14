from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from config.database import get_db
from models.petmodel import PetModel
from dto.petschema import PetSchema
from models.usermodels import User
from config.hashing import Hashing
from config.token import get_currentUser



class PetService:
    def get_all_pet(db: Session):
        return db.query(PetModel).all()

    def create_pet(request: PetSchema, db: Session):
        
        # user_byid = (db.query(User).filter(User.id == user_id).first())
        
    
        new_pet = PetModel(
            caretaker_name=request.caretaker_name,
            name=request.name,
            age=request.age,
            breed=request.breed,
            gender=request.gender,
            height=request.height,
            weight=request.weight,
            color=request.color,
            medical_history=request.medical_history,
        )
        # new_pet.user_id = user_byid.id

        db.add(new_pet)
        db.commit()
        db.refresh(new_pet)

        return new_pet

    def show_pet(petid: int, db: Session):
        show_p = db.query(PetModel).filter(PetModel.id == petid).first()
        # userid = (db.query(User).filter(User.petid == show_p.id).all()) 
        

        response = {
            "id": show_p.id,
            "Care Taker": show_p.caretaker_name,
            "name": show_p.name,
            "age": show_p.age,
            "breed": show_p.breed,
            "height": show_p.height,
            "weight": show_p.weight,
            "color": show_p.color,
            "medical_history": show_p.medical_history,
            # "user_id": user_id, 
        }

        return response

    # Lanjutlagi
    def update_pet(petid: int, request: PetSchema, db: Session):
        pet_id = db.query(PetModel).filter(PetModel.id == petid).first()

        pet_id.caretaker_name = request.caretaker_name
        pet_id.name = request.name
        pet_id.age = request.age
        pet_id.breed = request.breed
        pet_id.gender = request.gender
        pet_id.height = request.height
        pet_id.weight = request.weight
        pet_id.color = request.color
        pet_id.medical_history = request.medical_history
        db.commit()

        return pet_id

    def delete_pet(petid: int, db: Session):
        del_pet = (
            db.query(PetModel).filter(PetModel.id == petid).first()
        )

        db.delete(del_pet)
        db.commit()

        return "Done"

