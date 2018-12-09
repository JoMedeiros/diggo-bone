#!/usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser(description='Return a list of folders and files given a path as argument.')
parser.add_argument('path', metavar='P', type=str, nargs='+',
                    help='a path to search for files')

args = parser.parse_args()
#tree = {}

def json_tree(path,tabs):
    tree = '[\n'
    children = os.listdir(path)
    for c in children:
        for i in range(tabs):
            tree=tree+' '
        if (os.path.isfile(path+'/'+c)):
            size = os.path.getsize(path+'/'+c)
            tree=tree+('{"name": "'+c+ '" , "size": "'+str(size)+' KB"}' )
        else:
            tree=tree+('{"name": "'+c+'" ,"children": '+json_tree(path+'/'+c,tabs+1)
                    +'}')
        if c is not children[-1]:
            tree=tree+',\n'
    return tree + ']'

for p in args.path:
    print(json_tree(p, 0))


