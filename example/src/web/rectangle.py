from fastapi import APIRouter
from model.rectangle import Rectangle
import fake.rectangle as service

router = APIRouter(prefix = "/rectangle")

@router.get("/")
def get_all() -> list[Rectangle]:
    return service.get_all()
    
@router.get("/{color}")
def get_one(color) -> Rectangle | None:
    return service.get_one(color)
    
@router.post("/")
def create(rectangle: Rectangle) -> Rectangle:
    return service.create(rectangle)
    
@router.patch("/")
def modify(rectangle: Rectangle) -> Rectangle:
    return service.modify(rectangle)
    
@router.put("/")
def replace(rectangle: Rectangle) -> Rectangle:
    return service.replace(rectangle)
    
@router.delete("/{color}")
def delete(color: str):
    return service.delete(color)

@router.get("/area/")
def get_area(color: str) -> float:
    return service.area(color)

@router.get("/perimeter/")
def get_perimeter(color: str) -> float:
    return service.perimeter(color)

@router.get("/getColor/")
def get_color(height: float, width: float) -> str | None:
    return service.get_color(height, width)