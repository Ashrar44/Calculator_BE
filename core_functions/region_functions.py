# Region related endpoints
from fastapi import HTTPException


async def get_countries():
    """Get all countries"""
    try:
       result = [
           {"id": 1, "name": "United States"},
           {"id": 2, "name": "Canada"},
           {"id": 3, "name": "Mexico"}]
       return {'success': True, 'data': result}
    except Exception as e:
        raise HTTPException(status_code=500, detail={'success': False, 'message': str(e)})