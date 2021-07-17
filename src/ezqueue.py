from collections import deque


class ezqueue:
    def __init__(self, size):
        self.max_size = size
        self.queue = deque(maxlen=size)

    def put(self, id, data):
        itemRes = self.getById(id)

        if itemRes is None:
            self.queue.append({
                "_id": id,
                "data": data
            })
        else:
            del self.queue[self.queue.index(itemRes)]
            self.queue.append({
                "_id": id,
                "data": data
            })

    def getQueue(self):
        return self.queue

    def getById(self, id):
        itemRes = [x for x in self.queue if x["_id"] == id]
        if len(itemRes) <= 0:
            return None
        else:
            return itemRes[0]
