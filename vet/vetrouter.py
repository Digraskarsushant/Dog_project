from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.vetschema import VetSchema
from config.database import get_db
from .vetservices import VetService

router = APIRouter(prefix="/vet", tags=["Vet"])


@router.get("/")
def getallVet(db: Session = Depends(get_db)):
    return VetService.get_all_vet(db=db)


@router.post("/")
def createProduct(request: VetSchema, db: Session = Depends(get_db)):
    return VetService.create_vet(request=request, db=db)


@router.get("/{vetid}")
def showVet(vetid: int, db: Session = Depends(get_db)):
    return VetService.show_vet(vetid=vetid, db=db)


@router.put("/{vetid}")
def updateVet(
    vetid: int, request: VetSchema, db: Session = Depends(get_db)):
    return VetService.update_vet(vetid=vetid, request=request, db=db)


@router.delete("/{vetid}")
def deleteVet(vetid: int, db: Session = Depends(get_db)):
    return VetService.delete_vet(vetid=vetid, db=db)

