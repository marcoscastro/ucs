# encoding:utf-8

# This file implements a priority queue using heapq module
# Author: Marcos Castro

import heapq

class PriorityQueue:

	def __init__(self):
		self._queue = []
		self._index = 0

	def insert(self, item, priority):
		heapq.heappush(self._queue, (priority, self._index, item))
		self._index += 1

	def remove(self):
		return heapq.heappop(self._queue)[-1]

	def is_empty(self):
		return len(self._queue) == 0


# test...
# queue = PriorityQueue()
# queue.insert('e', 9)
# queue.insert('a', 2)
# queue.insert('h', 13)
# queue.insert('e', 5)
# queue.insert('c', 11)
# print(queue.remove())