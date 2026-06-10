from fastapi import APIRouter

router = APIRouter()

DB = []

@router.get("/")
def get_vehicles():
    return DB

@router.post("/")
def create_vehicle(vehicle: dict):
    DB.append(vehicle)
    return vehicle