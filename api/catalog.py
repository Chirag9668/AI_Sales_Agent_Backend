from fastapi import APIRouter

from tools.catalog_tool import load_catalog

router = APIRouter()


@router.get("/catalog")
def get_catalog():

    return load_catalog()