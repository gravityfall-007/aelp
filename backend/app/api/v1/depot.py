from fastapi import APIRouter

router = APIRouter()

DB = []

@router.get("/")
def get_depots():
    return DB

@router.post("/")
def create_depot(depot: dict):
    DB.append(depot)
    return depot