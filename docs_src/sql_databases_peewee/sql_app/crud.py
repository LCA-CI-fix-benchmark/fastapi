from . import models, schemas
### Summary of Changes:
1. Import the necessary models module to access the `User` model in the `crud.py` file.
2. Verify the correct method to filter and retrieve data from the `User` model in the provided functions.
3. Ensure that the `models.User` filter method is used appropriately to retrieve user data based on the specified conditions.
def create_user(user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db_user.save()
    return db_user


def get_items(skip: int = 0, limit: int = 100):
    return list(models.Item.select().offset(skip).limit(limit))


def create_user_item(item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db_item.save()
    return db_item
