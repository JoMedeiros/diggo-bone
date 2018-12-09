#!/usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser(description='Return a list of folders and files given a path as argument.')
parser.add_argument('path', metavar='P', type=str, nargs='+',
                    help='a path to search for files')

args = parser.parse_args()

def rec_json_tree(path,tabs=1,sep='\t'):
    #tree = '{\n'
    tree =''
    children = os.listdir(path)
    for c in children:
        tree += (tabs*sep)+'"'+c+'":\n' # The name
        if (os.path.isfile(path+'/'+c)):
            size = os.path.getsize(path+'/'+c)
            timestamp = str(os.stat(path+'/'+c).st_mtime)
            tree+=tabs*sep+('{\n'
                +(tabs+1)*sep+'"type": "file",\n'
                +(tabs+1)*sep+'"status": "idle",\n'
                +(tabs+1)*sep+'"size": "'+str(size)+' KB"\n'
                +tabs*sep+'}')
        elif not os.listdir(path+'/'+c):
            tree+=tabs*sep+('{\n'+
                    (tabs+1)*sep+'"type": "empty_dir"\n'+
                    tabs*sep+'}')
        else:
            tree+=tabs*sep+('{\n'
                +(tabs+1)*sep+'"type": "dir",\n'
                +(tabs+1)*sep+'"status": "idle",\n'
                +rec_json_tree(path+'/'+c,tabs+1) # Files and subdirs
                +tabs*sep+'}')
        if c is not children[-1]:
            tree+=','
        tree+='\n'
    return tree
    #+(tabs-1)*sep+'close}'

def json_tree(p):
    return '{\n'+rec_json_tree(p)+'}'

for p in args.path:
    print(json_tree(p))


