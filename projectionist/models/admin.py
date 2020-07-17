from projectionist.models.channel import (
    Channel,
)


ITEM_LIST = [
    ("Channel", Channel),
]

class AdminPage():

    @classmethod
    async def get_list(cls):
        rs = []
        for key, _cls in ITEM_LIST:
            item = {
                "name": key,
                "count": await _cls.count(),
            }
            rs.append(item)
        return rs