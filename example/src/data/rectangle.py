from data.init import curs
from model.rectangle import Rectangle

curs.execute("""create table if not exists rectangle(
                color REAL)""")


def row_to_model(row: tuple) -> Rectangle:
    color = row[0]
    return Rectangle(color=color)

def model_to_dict(rectangle: Rectangle) -> dict:
    print(rectangle.model_dump())
    return rectangle.model_dump()

def get_one(color: float) -> Rectangle:
    qry = "select * from rectangle where color=:color"
    params = {"color": color}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Rectangle]:
    qry = "select * from rectangle"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(rectangle: Rectangle):
    qry = """INSERT INTO rectangle VALUES (:color)"""
    params = model_to_dict(rectangle)
    curs.execute(qry, params)
    return rectangle

def modify(rectangle: Rectangle):
    return rectangle

def replace(rectangle: Rectangle):
    return rectangle

def delete(rectangle: Rectangle):
    qry = "delete from rectangle where color=:color"
    params = {"color": rectangle.color}
    curs.execute(qry, params)