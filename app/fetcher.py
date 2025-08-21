from typing import Any, Dict, List, Optional

from pymongo import AsyncMongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import PyMongoError


class DataLoader:

    def __init__(self, mongo_uri: str, db_name: str, collection_name: str):
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self.collection_name = collection_name
        self.client: Optional[AsyncMongoClient] = None
        self.db: Optional[Database] = None
        self.collection: Optional[Collection] = None

    async def connect(self):

        try:
            self.client = AsyncMongoClient(
                self.mongo_uri, serverSelectionTimeoutMS=5000
            )
            await self.client.admin.command("ping")
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]

            await self._setup_indexes()
        except PyMongoError as e:

            self.client = None
            self.db = None
            self.collection = None
    async def _setup_indexes(self):

        if self.collection is not None:
            try:
                await self.collection.create_index("ID", unique=True)

            except PyMongoError as e:
                pass

    def disconnect(self):

        if self.client:
            self.client.close()

    async def get_all_data(self) -> List[Dict[str, Any]]:

        if self.collection is None:
            raise RuntimeError("Database connection is not available.")

        try:
            items: List[Dict[str, Any]] = []
            async for item in self.collection.find({}):
                item["_id"] = str(item["_id"])
                items.append(item)
            return items
        except PyMongoError as e:
            raise RuntimeError(f"Database operation failed: {e}")

# from pymongo import