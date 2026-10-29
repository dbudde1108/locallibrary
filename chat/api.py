# chat/api.py
from ninja import Router

router = Router(tags=["rooms"])


@router.get("/", response=list[RoomOut])
@paginate
def list_rooms(request, filters: Query[RoomFilter]):
    ...


@router.get("/{room_id}", response=RoomOut)
def get_room(request, room_id: int):
    ...

# ... and the rest
