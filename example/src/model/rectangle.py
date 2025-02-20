from pydantic import BaseModel, Field

class Rectangle(BaseModel):
    width: float = Field(gt=0, default=1)
    height: float = Field(gt=0, default=1)
    color: str = Field(default=None)
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)