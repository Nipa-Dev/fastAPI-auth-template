from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


items = {
    1: {
        "item_name": "Apple",
        "item_detail": "A fruit"
    },
    2: {
        "item_name": "Banana",
        "item_detail": "A fruit"
    },
    3: {
        "item_name": "Carrot",
        "item_detail": "A vegetable"
    },
    4: {
        "item_name": "Potato",
        "item_detail": "A root vegetable"
    },
    5: {
        "item_name": "Egg",
        "item_detail": "A food item"
    },
    6: {
        "item_name": "Chicken",
        "item_detail": "A meat product"
    },
    7: {
        "item_name": "Rice",
        "item_detail": "A staple food"
    },
    8: {
        "item_name": "Wheat",
        "item_detail": "A cereal grain"
    },
    9: {
        "item_name": "Milk",
        "item_detail": "A dairy product"
    },
    10: {
        "item_name": "Coffee",
        "item_detail": "A hot beverage"
    }
}


@router.get("/")
async def read_items():
    return items