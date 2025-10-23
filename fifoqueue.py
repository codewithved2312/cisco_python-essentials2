class QueueError(IndexError):   # Inherit from a built-in exception (IndexError fits well)
    pass


class Queue:
    def __init__(self):
        self.__queue = []       # Private list to hold elements

    def put(self, elem):
        self.__queue.insert(0, elem)   # Insert at the beginning (FIFO order)

    def get(self):
        if len(self.__queue) == 0:
            raise QueueError("Queue is empty!")  # Raise custom error
        return self.__queue.pop()                # Remove from the end (FIFO)


# --- Testing ---
que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):  # One more than available → will trigger error
        print(que.get())
except QueueError:
    print("Queue error")
