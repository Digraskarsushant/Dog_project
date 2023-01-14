from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.petschema import PetSchema
from models.usermodels import User
from config.token import get_currentUser
from config.database import get_db

from .petservices import PetService

router = APIRouter(prefix="/pet", tags=["Pet"])


@router.get("/")
def getallPet(db: Session = Depends(get_db)):
    return PetService.get_all_pet(db=db)


@router.post("/")
def createPet(request: PetSchema, db: Session=Depends(get_db),):
    return PetService.create_pet(request=request, db=db)


@router.get("/{petid}")
def showPet(petid: int, db: Session = Depends(get_db)):
    return PetService.show_pet(petid=petid, db=db)


@router.put("/{petid}")
def updatePet(
    petid: int, request: PetSchema, db: Session = Depends(get_db)
):
    return PetService.update_pet(petid=petid, request=request, db=db)


@router.delete("/{petid}")
def deletePet(petid: int, db: Session = Depends(get_db)):
    return PetService.delete_pet(petid=petid, db=db)

