from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.storeschema import StoreBase
from config.database import get_db

from .storeservice import StoreService

router = APIRouter(prefix="/store", tags=["Store"])


@router.get("/")
def getallStore(db: Session = Depends(get_db)):
    return StoreService.get_all_store(db=db)


@router.post("/")
def createStore(request: StoreBase, db: Session = Depends(get_db)):
    return StoreService.create_store(request=request, db=db)


@router.get("/{storeid}")
def showStore(storeid: int, db: Session = Depends(get_db)):
    return StoreBase.show_store(storeid=storeid, db=db)


@router.put("/{storeid}")
def updateStore(
    storeid: int, request: StoreBase, db: Session = Depends(get_db)
):
    return StoreService.update_store(storeid=storeid, request=request, db=db)


@router.delete("/{storeid}")
def deletestore(storeid: int, db: Session = Depends(get_db)):
    return StoreService.delete_store(storeid=storeid, db=db)
