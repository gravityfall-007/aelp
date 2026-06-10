from fastapi import APIRouter

router = APIRouter()

DB = []

@router.get("/")
def get_demand():
    return DB

@router.post("/")
def create_demand(demand: dict):
    DB.append(demand)
    return demand