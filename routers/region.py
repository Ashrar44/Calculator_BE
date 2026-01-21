# Region endpoints router
from fastapi import APIRouter
from core_functions.region_functions import (get_countries)

router = APIRouter(prefix="/regions", tags=["Regions"])

@router.get("/get-countries")
async def get_countries_route():
    """Get all countries"""
    return await get_countries()