from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.serviceschema import Service
from config.database import get_db

from .serviceservice import ServiceService

router = APIRouter(prefix="/service", tags=["Services"])


@router.get("/")
def getallService(db: Session = Depends(get_db)):
    return ServiceService.get_all_service(db=db)


@router.post("/")
def createService(request: Service, db: Session = Depends(get_db)):
    return ServiceService.create_service(request=request, db=db)


@router.get("/{serviceid}")
def showService(serviceid: int, db: Session = Depends(get_db)):
    return ServiceService.show_service(serviceid=serviceid, db=db)


@router.put("/{serviceid}")
def updateService(
    serviceid: int, request: Service, db: Session = Depends(get_db)
):
    return ServiceService.update_service(serviceid=serviceid, request=request, db=db)


@router.delete("/{serviceid}")
def deleteservice(serviceid: int, db: Session = Depends(get_db)):
    return ServiceService.delete_service(serviceid=serviceid, db=db)
