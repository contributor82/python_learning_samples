# List as Queue
# Queue - First In, First Out

from collections import deque

queue = deque({"Eric", "John", "Merry"})

print("Initial Queue elements: ", queue)

queue.append("Terry")
queue.append("Graham")

print("After appending multiple elements in queue: ", queue)

queue.popleft()
queue.popleft()
print("After popping left multiple elements in queue: ", queue)

