#!/usr/bin/env python3

import json
import os
import datetime

# TODO : first case
class Diggo_directory_manager:

	def __init__ (self, side, dirpath):
		self.SIDE = side
		self.SYNC_TREE = ''
		self.CURRENT_TREE = ''
		self.DIRPATH = dirpath

		self.load_tree(firstime=True)

	# REVIEW : edit timestamp tag
	def rec_json_tree(self, dirpath,tabs=1,sep=' '):
		"""
		função recursiva auxiliar que gera uma string formatada para ser interpretada
		pelo modulo json como um dicionário informando descrevendo
		um diretório 'dirpath' em formato de árvore. OBS: adicionar as chaves externas para funcionar.
		"""

		tree =''
		children = os.listdir(dirpath)
		for c in children:
			tree += (tabs*sep)+'"'+c+'":\n' # The name
			time_stamp = os.stat(dirpath+'/'+c).st_mtime
			ts_datetime = datetime.datetime.utcfromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
			if (os.path.isfile(dirpath+'/'+c)):
				size = os.path.getsize(dirpath+'/'+c)
				tree+=tabs*sep+('{\n'
					+(tabs+1)*sep+'"type": "file",\n'
					+(tabs+1)*sep+'"status": "idle",\n'
					+(tabs+1)*sep+'"size_bytes": "'+str(size)+'",\n'
					+(tabs+1)*sep+'"timestamp": '+str(time_stamp)+',\n'
					+(tabs+1)*sep+'"datetime": \"'+str(ts_datetime)+'\"\n'
					+tabs*sep+'}')
			elif not os.listdir(dirpath+'/'+c):
				tree+=tabs*sep+('{\n'+
					(tabs+1)*sep+'"type": "empty_dir"\n'+
					tabs*sep+'}')
			else:
				tree+=tabs*sep+('{\n'
					+(tabs+1)*sep+'"type": "dir",\n'
					+(tabs+1)*sep+'"status": "idle",\n'
					+(tabs+1)*sep+'"timestamp": '+str(time_stamp)+',\n'
					+(tabs+1)*sep+'"datetime": \"'+str(ts_datetime)+'\",\n'
					+(tabs+1)*sep+('"children":\n'
						+(tabs+1)*sep+'{\n'
						+self.rec_json_tree(dirpath+'/'+c,tabs+2)) # Files and subdirs
					+(tabs+1)*sep+'}\n'+(tabs*sep)+'}')
			if c is not children[-1]:
				tree+=','
			tree+='\n'
		return tree

	def load_tree(self, treename="CURRENT_TREE", firstime=False):
		"""
		generates a dict with info about the tree 'treename' from a .json file.
		"""	
		if not firstime:
			f = open(treename.lower() + ".json", 'r')
			tree_dict = json.loads(f.read())
			f.close() # close file handler
		else:
			self.gen_current_tree()
			self.SYNC_TREE = self.CURRENT_TREE


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
		updates self.CURRENT_TREE.
		"""

		rec_tree = self.rec_json_tree(self.DIRPATH)
		tree = "{\n" + rec_tree + "}"
		self.CURRENT_TREE = json.loads(tree)


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

# TEST
if __name__ == "__main__":
	TREE_MAN = Diggo_directory_manager(side='TEST', dirpath='test_directory')
	print(str(TREE_MAN.CURRENT_TREE))

	print('Exiting...')