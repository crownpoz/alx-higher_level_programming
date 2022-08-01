#!/usr/bin/python3
'''Defines an object attribute look up function'''


def lookup(obj):
    '''returns a list of an objects available''' 
    return (dir(obj))
