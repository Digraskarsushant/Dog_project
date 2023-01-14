from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from config.database import get_db
from models.servicemodel import ServiceModel
from dto.serviceschema import Service
from config.hashing import Hashing


class ServiceService:
    def get_all_service(db: Session):
        return db.query(ServiceModel).all()

    def create_service(request: Service, db: Session):
        new_service = ServiceModel(
            name=request.name,
            description=request.description,
        )

        db.add(new_service)
        db.commit()
        db.refresh(new_service)

        return new_service

    def show_service(serviceid: int, db: Session):
        show_s = db.query(ServiceModel).filter(ServiceModel.id == serviceid).first()

        response = {
            "id": show_s.id,
            "name": show_s.name,
            "description": show_s.description,
        }

        return response

    # Lanjutlagi
    def update_service(serviceid: int, request: Service, db: Session):
        service_id = db.query(ServiceModel).filter(ServiceModel.id == serviceid).first()

        service_id.name = request.name
        service_id.description = request.description
        db.commit()

        return service_id

    def delete_service(serviceid: int, db: Session):
        del_service = (
            db.query(ServiceModel).filter(ServiceModel.id == serviceid).first()
        )

        db.delete(del_service)
        db.commit()

        return "Done"

