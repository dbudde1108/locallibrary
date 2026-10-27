# locallibrary_config/api.py
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello")
def hello(request, name: str = "world"):
    return {"message": f"Hello, {name}!"}


# locallibrary_config/api.py
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
