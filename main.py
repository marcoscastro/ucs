# encoding:utf-8

# This file implements the Uniform Cost Search (UCS) algorithm
# Explanation of UCS algorithm: https://www.youtube.com/watch?v=AaKEW_mVBtg
# Author: Marcos Castro

import time
from graph import *
from priority_queue import *

def run(graph, key_node_start, key_node_goal, verbose=False, time_sleep=0):
	if key_node_start not in graph.getNodes() or key_node_goal not in graph.getNodes():
		print('Error: key_node_start \'%s\' or key_node_goal \'%s\' not exists!!' % (key_node_start, key_node_goal))
	else:
		# UCS uses priority queue, priority is the cumulative cost (smaller cost)
		queue = PriorityQueue()

		# expands initial node

		# get the keys of all successors of initial node
		keys_successors = graph.getSuccessors(key_node_start)

		# adds the keys of successors in priority queue
		for key_sucessor in keys_successors:
			weight = graph.getWeightEdge(key_node_start, key_sucessor)
			# each item of queue is a tuple (key, cumulative_cost)
			queue.insert((key_sucessor, weight), weight)


		reached_goal, cumulative_cost_goal = False, -1
		while not queue.is_empty():
			# remove item of queue, remember: item of queue is a tuple (key, cumulative_cost)
			key_current_node, cost_node = queue.remove() 
			if(key_current_node == key_node_goal):
				reached_goal, cumulative_cost_goal = True, cost_node
				break

			if verbose:
				# shows a friendly message
				print('Expands node \'%s\' with cumulative cost %s ...' % (key_current_node, cost_node))
				time.sleep(time_sleep)

			# get all successors of key_current_node
			keys_successors = graph.getSuccessors(key_current_node)

			if keys_successors: # checks if contains successors
				# insert all successors of key_current_node in the queue
				for key_sucessor in keys_successors:
					cumulative_cost = graph.getWeightEdge(key_current_node, key_sucessor) + cost_node
					queue.insert((key_sucessor, cumulative_cost), cumulative_cost)

		if(reached_goal):
			print('\nReached goal! Cost: %s\n' % cumulative_cost_goal)
		else:
			print('\nUnfulfilled goal.\n')


if __name__ == "__main__":

	# build the graph...
	# adds nodes in the graph
	graph = Graph()
	graph.addNode('S') # start
	graph.addNode('a')
	graph.addNode('b')
	graph.addNode('c')
	graph.addNode('d')
	graph.addNode('e')
	graph.addNode('f')
	graph.addNode('G') # goal
	graph.addNode('h')
	graph.addNode('p')
	graph.addNode('q')
	graph.addNode('r')
	# linking the nodes
	graph.connect('S', 'd', 3)
	graph.connect('S', 'e', 9)
	graph.connect('S', 'p', 1)
	graph.connect('b', 'a', 2)
	graph.connect('c', 'a', 2)
	graph.connect('d', 'b', 1)
	graph.connect('d', 'c', 8)
	graph.connect('d', 'e', 2)
	graph.connect('e', 'h', 8)
	graph.connect('e', 'r', 2)
	graph.connect('f', 'c', 3)
	graph.connect('f', 'G', 2)
	graph.connect('h', 'p', 4)
	graph.connect('h', 'q', 4)
	graph.connect('p', 'q', 15)
	graph.connect('r', 'f', 1)

	run(graph=graph, key_node_start='S', key_node_goal='G', verbose=True, time_sleep=2)