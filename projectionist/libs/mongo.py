import motor.motor_asyncio
from projectionist.config import (MONGO_URI,CLIENT_COLLECTION)



client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db_projectionist = client[CLIENT_COLLECTION]
