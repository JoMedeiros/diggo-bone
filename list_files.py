#!/usr/bin/env python3

import os
import argparse

def rec_json_tree(path,tabs=1,sep='\t'):
    #tree = '{\n'
    tree =''
    children = os.listdir(path)
    for c in children:
        tree += (tabs*sep)+'"'+c+'":\n' # The name
        timestamp = str(os.stat(path+'/'+c).st_mtime)
        #timestamp = str(os.path.getmtime(path+'/'+c))
        if (os.path.isfile(path+'/'+c)):
            size = os.path.getsize(path+'/'+c)
            tree+=tabs*sep+('{\n'
                +(tabs+1)*sep+'"type": "file",\n'
                +(tabs+1)*sep+'"status": "idle",\n'
                +(tabs+1)*sep+'"size": "'+str(size)+' KB",\n'
                +(tabs+1)*sep+'"timestamp": '+timestamp+'\n'
                +tabs*sep+'}')
        elif not os.listdir(path+'/'+c):
            tree+=tabs*sep+('{\n'+
                    (tabs+1)*sep+'"type": "empty_dir"\n'+
                    tabs*sep+'}')
        else:
            tree+=tabs*sep+('{\n'
                +(tabs+1)*sep+'"type": "dir",\n'
                +(tabs+1)*sep+'"status": "idle",\n'
                +(tabs+1)*sep+'"timestamp": '+timestamp+',\n'
                +rec_json_tree(path+'/'+c,tabs+1) # Files and subdirs
                +tabs*sep+'}')
        if c is not children[-1]:
            tree+=','
        tree+='\n'
    return tree

def json_tree(p):
    return '{\n'+rec_json_tree(p)+'}'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Return a list of folders and files given a path as argument.')
    parser.add_argument('path', metavar='P', type=str, nargs='+',
                        help='a path to search for files')
    
    args = parser.parse_args()

    for p in args.path:
        print(json_tree(p))

