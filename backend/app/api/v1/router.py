from fastapi import APIRouter
from app.api.v1 import auth, fleet, depot, demand

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(fleet.router, prefix="/fleet", tags=["fleet"])
api_router.include_router(depot.router, prefix="/depots", tags=["depots"])
api_router.include_router(demand.router, prefix="/demand", tags=["demand"])