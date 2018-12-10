#!/usr/bin/env python3

def get_diff_tree(current_tree):
	"""
	generates a dict that says whats different between the current directory state
	to the last state before syncing.
	"""

	pass

def get_tree():
	"""
	generates a dict with info about the current directory (new files/directories,
	modifications).
	"""	

	pass

def save_tree():
	""" 
	writes a .json file from dictionary that represents the definitive
	directory tree informations by now
	"""

	pass

def get_sync_tree(diff_tree_server, diff_tree_client):
	"""
	returns a dictionary that represents the definitive
	directory tree after comparing the modifications between server and client
	"""

	pass	

def apply_changes(sync_tree):
	"""
	updates current directory tree based on a json representing
	the new directory tree.
	"""

	pass


if __name__ == "__main__":
	print('Exiting...')