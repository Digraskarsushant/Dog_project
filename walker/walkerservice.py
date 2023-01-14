from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from config.database import get_db
from models.walkermodels import WalkerModel
from dto.walkerschema import RegisterWalker
from config.hashing import Hashing


class WalkerService:
    def get_all_walker(db: Session):
        return db.query(WalkerModel).all()

    def create_walker(request: WalkerModel, db: Session):
        new_walker = WalkerModel(
            name=request.name,
            email=request.email,
            mobile=request.mobile,
            address=request.address,
            driving_license=request.driving_license,
            time_dur=request.time_dur,
            days=request.days
        )

        db.add(new_walker)
        db.commit()
        db.refresh(new_walker)

        return new_walker

    def show_walker(walkerid: int, db: Session):
        show_w = db.query(WalkerModel).filter(WalkerModel.id == walkerid).first()

        response = {
            "ID": show_w.id,
            "Name": show_w.name,
            "Email": show_w.email,
            "Mobile": show_w.mobile,
            "Address": show_w.address,
            "Driving_license": show_w.driving_license,
            "Time Duration": show_w.time_dur,
            "Days": show_w.days,
        }

        return response

    # Lanjutlagi
    def update_walker(walkerid: int, request: WalkerModel, db: Session):
        walker_id = db.query(WalkerModel).filter(WalkerModel.id == walkerid).first()

        walker_id.name = request.name
        walker_id.email = request.email
        walker_id.mobile = request.mobile
        walker_id.address = request.address
        walker_id.driving_license = request.driving_license
        walker_id.time_dur = request.time_dur
        walker_id.days = request.days
        db.commit()

        return walker_id

    def delete_walker(walkerid: int, db: Session):
        del_walker = (
            db.query(WalkerModel).filter(WalkerModel.id == walkerid).first()
        )

        db.delete(del_walker)
        db.commit()

        return "Done"

