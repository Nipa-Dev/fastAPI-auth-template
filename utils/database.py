import asyncpg

from .constants import Server


class Connection:
    """Connection configuration for postgresql database"""

    DATABASE_URL = Server.DB_URL

    DB_POOL = asyncpg.create_pool(DATABASE_URL)