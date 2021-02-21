import arrow
import pymongo
import ujson
import  re
import bson
from bson.objectid import ObjectId
from projectionist.libs.mongo import db_projectionist

class Channel():

    def __init__(self, **kwargs):
        self.obj = kwargs
        self._id = kwargs['_id']
        self.id = str(self._id)
        self._changed = {}

    @classmethod
    async def create(
        cls, 
        name,
        ):
        now = arrow.utcnow().datetime
        data = {
            "name": name,
        }
        r = await db_projectionist.channel.insert_one(data)
        if not r.acknowledged:
            return None
        data['_id'] = r.inserted_id
        return cls(**data)

    async def save(self):
        query = {"_id": self._id}
        data = {"$set": self._changed}
        r = await db_projectionist.channel.update_one(query, data)
        if not r.acknowledged:
            return None
        self._changed = {}
        return True
    
    async def edit(self, data):
        for key in data:
            value = data[key]
            self._changed[key] = value
        return await self.save()

    @classmethod
    async def get_multi(cls, query=None, offset=0, count=10, sort=None):
        if query is None:
            query = {}
        if offset < 0:
            offset = 0
        if sort is None:
            sort = [('_id', pymongo.DESCENDING)]
        rs = []
        cursor = db_projectionist.channel.find(query, sort=sort).skip(offset).limit(count)
        async for document in cursor:
            rs.append(document)
        return [cls(**r) for r in rs]

    @classmethod
    async def get(cls, id):
        try:
            oid = ObjectId(id)
        except bson.errors.InvalidId as e:
            return None
        document = await db_projectionist.channel.find_one({"_id": oid})
        if not document:
            return None
        return cls(**document)

    @classmethod
    async def count(cls, query=None):
        if query is None:
            query = {}
        if query == {}:
            return await db_projectionist.channel.estimated_document_count()
        return await db_projectionist.channel.count_documents(query)

    @classmethod
    async def delete_multi(cls, ids):
        oids = [ObjectId(id) for id in ids]
        result = await  db_projectionist.channel.delete_many({'_id': {'$in': oids}})
        if result.acknowledged:
            return True
        return False
    

    def to_json(self):
        created_at = arrow.get(self.created_at)
        updated_at = arrow.get(self.updated_at)
        r = {
            "_id": str(self._id),
            "name": self.name,
        }
        return r
