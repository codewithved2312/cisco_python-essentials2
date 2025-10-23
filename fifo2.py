class QueueError(IndexError):   # base exception for empty queue
    pass


class Queue:
    def __init__(self):
        self.__queue = []       # private list to hold items

    def put(self, elem):
        self.__queue.insert(0, elem)   # add at front (FIFO)

    def get(self):
        if len(self.__queue) == 0:
            raise QueueError("Queue is empty!")
        return self.__queue.pop()      # remove from end (FIFO)

    # helper to check internal length (for subclass)
    def _length(self):
        return len(self.__queue)


class SuperQueue(Queue):
    def isempty(self):
        return self._length() == 0     # returns True if queue is empty


# --- Testing ---
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
