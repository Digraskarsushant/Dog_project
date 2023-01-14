from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.groomingschema import groomingschema
from config.database import get_db

from .groomingservices import GroomingService

router = APIRouter(prefix="/grooming", tags=["grooming"])


@router.get("/")
def getallgrooming(db: Session = Depends(get_db)):
    return GroomingService.get_all_grooming(db=db)


@router.post("/")
def creategrooming(request: groomingschema, db: Session = Depends(get_db)):
    return GroomingService.create_grooming(request=request, db=db)


@router.get("/{groomingid}")
def showgrooming(groomingid: int, db: Session = Depends(get_db)):
    return GroomingService.show_grooming(groomingid=groomingid, db=db)


@router.put("/{groomingid}")
def updategrooming(
    groomingid: int, request: groomingschema, db: Session = Depends(get_db)
):
    return GroomingService.update_grooming(groomingid=groomingid, request=request, db=db)


@router.delete("/{groomingid}")
def deletegrooming(groomingid: int, db: Session = Depends(get_db)):
    return GroomingService.delete_grooming(groomingid=groomingid, db=db)

