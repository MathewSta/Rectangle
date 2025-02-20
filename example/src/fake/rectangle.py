from model.rectangle import Rectangle

_rectangles = [
    Rectangle(width=2, height=3, color="blue"),
    Rectangle(width=3.5, height=3, color="red"),
    Rectangle(width=4, height=1, color="green"),
    ]

def get_all() -> list[Rectangle]:
    """Return all Rectangles"""
    return _rectangles
    
def get_one(color: str) -> Rectangle | None:
    for _rectangle in _rectangles:
        if _rectangle.color == color:
            return _rectangle
    return None

def create(rectangle: Rectangle) -> Rectangle:
    """Add a Rectangle"""
    return rectangle

def modify(rectangle: Rectangle) -> Rectangle:
    """Modify a Rectangle"""
    return rectangle

def replace(rectangle: Rectangle) -> Rectangle:
    """Replace a Rectangle"""
    return rectangle

def delete(color: str) -> bool:
    """Delete a Rectangle"""
    return None

def area(color: str) -> float:
    """Area of the Rectangles"""
    for _rectangle in _rectangles:
        if _rectangle.color == color:
            return _rectangle.area()
    return None

def perimeter(color: str) -> float:
    """Perimeter of the Rectangles"""
    for _rectangle in _rectangles:
        if _rectangle.color == color:
            return _rectangle.perimeter()
    return None

def get_color(height: float, width: float) -> str | None:
    for _rectangle in _rectangles:
        if _rectangle.height == height:
            if _rectangle.width == width:
                return _rectangle.color
    return None