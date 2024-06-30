import random
import socket
import datetime

from loguru import logger
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.database import Connection
from routers import security, items

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        logger.info(f"Local network: http://{local_ip}:5001")
    except Exception:
        logger.error("Failure to get local network IP address.")
        logger.trace(
            "Startup failed to receive network IP address, proceeding anyways."
        )

    logger.info(f"Server started at: {datetime.datetime.now()}")

    # possible error that might happen: socket.gaierror, if it keeps persisting,
    # try adding try-except block to catch it and re-do the `await Connection.DB_POOL`
    # within the block

    # Create database connection pool
    await Connection.DB_POOL

    yield
    # closing down, anything after yield will be ran as shutdown event.
    await Connection.DB_POOL.close()
    logger.info(f"Server shutting down at: {datetime.datetime.now()}")


app = FastAPI(lifespan=lifespan)

app.include_router(security.router)
app.include_router(items.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["htpp://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.get("/hello")
async def get_random_number():
    return f"{random.randint(0, 100)} Hello World!"

#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run(app, host="localhost", port=5001)