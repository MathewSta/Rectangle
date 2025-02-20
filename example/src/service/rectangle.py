from model.rectangle import Rectangle
from fake import rectangle as data

def get_all() -> list[Rectangle]:
    return data.get_all()
    
def get_one(color: str) -> Rectangle | None:
    return data.get_one(color)

def create(rectangle: Rectangle) -> Rectangle:
    return data.create(rectangle)

def modify(rectangle: Rectangle) -> Rectangle:
    return data.modify(rectangle)

def replace(rectangle: Rectangle) -> Rectangle:
    return data.replace(rectangle)

def delete(color: str) -> bool:
    return data.delete(color)

def area(color: str) -> float:
    return data.area(color)

def perimeter(color: str) -> float:
    return data.perimeter(color)

def get_color(height: float, width: float) -> str | None:
    return data.get_color(height, width)