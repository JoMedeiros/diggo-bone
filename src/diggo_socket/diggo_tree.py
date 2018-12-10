#!/usr/bin/env python3

import json

# TODO : first case
class Diggo_directory_manager:

	def __init__ (self, side):
		self.SIDE = side
		self.SYNC_TREE = load_tree("SYNC_TREE")
		self.CURRENT_TREE = load_tree("CURRENT_TREE")


	def load_tree(self, treename):
		"""
		generates a dict with info about the tree 'treename' from a .json file.
		"""	
		
		f = open(treename.lower() + ".json", 'r')
		tree_dict = json.loads(f.read())

		f.close() # close file handler

		return tree_dict

	def save_tree(self, treename):
		"""
		generates a dict with info about the tree 'treename' from a .json file.
		"""	

		# choosing tree to save (DEFAULT to CURRENT_TREE)
		tree = self.CURRENT_TREE
		if treename == "SYNC_TREE":
			tree = self.SYNC_TREE

		f = open(treename.lower() + ".json", 'w')
		f.write(json.dumps(tree))

		f.close() # close file handler

	def gen_current_tree(self):
		"""
		generates a dict that says whats different between the current directory state
		to the last state before syncing.
		"""
		pass


	def get_diff_tree(self, current_tree):
		"""
		generates a dict that says whats it's going to be updated before generating the sync tree.
		"""

		pass

	def gen_sync_tree(self, diff_tree_server, diff_tree_client):
		"""
		returns a dictionary that represents the definitive
		directory tree after comparing the modifications between server and client
		"""

		pass

	def revert_current(self, sync_tree):
		"""
		resets the current directory to what it was right after the last sync
		"""

		pass

	def apply_changes(self, sync_tree):
		"""
		updates current directory tree based on a json representing
		the updated sync directory tree.
		"""

		pass


if __name__ == "__main__":
	print('Exiting...')