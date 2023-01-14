from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.walkerschema import RegisterWalker
from config.database import get_db

from .walkerservice import WalkerService

router = APIRouter(prefix="/walker", tags=["Walker"])


@router.get("/")
def getallWalker(db: Session = Depends(get_db)):
    return WalkerService.get_all_walker(db=db)


@router.post("/")
def createWalker(request: RegisterWalker, db: Session = Depends(get_db)):
    return WalkerService.create_walker(request=request, db=db)


@router.get("/{walkerid}")
def show_walker(walkerid: int, db: Session = Depends(get_db)):
    return WalkerService.show_walker(walkerid=walkerid, db=db)


@router.put("/{walkerid}")
def updateWalker(
    walkerid: int, request: RegisterWalker, db: Session = Depends(get_db)
):
    return WalkerService.update_walker(walkerid=walkerid, request=request, db=db)


@router.delete("/{walkerid}")
def deletewalker(walkerid: int, db: Session = Depends(get_db)):
    return WalkerService.delete_walker(walkerid=walkerid, db=db)
