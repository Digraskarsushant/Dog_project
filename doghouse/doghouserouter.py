from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.doghouseschema import RegisterDoghouse
from config.database import get_db
from .doghouseservice import DoghouseService

router = APIRouter(prefix="/doghouse", tags=["Doghouse"])


@router.get("/")
def getalldoghouse(db: Session = Depends(get_db)):
    return DoghouseService.get_all_doghouse(db=db)


@router.post("/")
def createDoghouse(request: RegisterDoghouse, db: Session = Depends(get_db)):
    return DoghouseService.create_doghouse(request=request, db=db)


@router.get("/{doghouseid}")
def showDoghouse(doghouseid: int, db: Session = Depends(get_db)):
    return DoghouseService.show_doghouse(doghouseid=doghouseid, db=db)


@router.put("/{doghouseid}")
def updateDoghouse(
    doghouseid: int, request: RegisterDoghouse, db: Session = Depends(get_db)):
    return DoghouseService.update_doghouse(doghouseid=doghouseid, request=request, db=db)


@router.delete("/{doghouseid}")
def deleteDoghouse(doghouseid: int, db: Session = Depends(get_db)):
    return DoghouseService.delete_doghouse(doghouseid=doghouseid, db=db)

