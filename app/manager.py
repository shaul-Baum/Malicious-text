import os
from fetcher import DataLoader
import asyncio
from processor import Processor

# קבלת פרטי החיבור מ־environment variables, עם ברירות מחדל
MONGO_URI = "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"


MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "IranMalDB")  # שים לב: DB הנכון
MONGO_COLLECTION_NAME = os.getenv("tweets", "data")  # הקולקשן הנכון

data_loader = DataLoader(
    mongo_uri=MONGO_URI,
    db_name="IranMalDB",
    collection_name="tweets"
)

async def main():
    await data_loader.connect()
    data = await data_loader.get_all_data()
    a = Processor(data)
    return a.manager()
if __name__ == "__main__":
    print(asyncio.run(main()))
