## FastAPI simple auth template

This project uses postgreSQL database and uses OAuth2 for auth system. This template project is tailored for my use cases.

There is example file called `req.py` that contains example on how to make requests to `/token`  and `/authenticate` to receive refresh token and access token.

The DB user schema can be found in `postgres/init.sql` that contains USER table. The project does **NOT** create user automatically yet.

Required packages can be found in `requirements.txt`

### Using the authentication to protect endpoints.
You can easily use the authentication to protect endpoints. That requires the user to pass `access_token`. This can be done like this: 
```py
# You don't need to use APIRouter
from fastAPI import APIRouter

from utils.auth import User, get_current_active_user


router = APIRouter()

@router.get("/example/protected")
async def example_protected_endpoint(current_user: Annotated[User, Depends(get_current_active_user)],)
    # current_user contains all the user information, and can be used if needed to perform actions.
    return "You have accessed the endpoint!"
```