#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:21:02 2024

@author: vaibhav
"""

'''

def dfs(graph, start, goal):
    visited = set()
    path = []
    
    def dfs_recursive(current):
        visited.add(current)
        path.append(current)
        
        if current == goal:
            return True
            
        for neighbor in graph[current]:
            if neighbor not in visited:
                if dfs_recursive(neighbor):
                    return True
        path.pop()
        return False
    
    dfs_recursive(start)
    return path




graph={ 'A':['B','c'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':['F'],
'F':[] 
}

start='A'

goal='F'

dfs(graph,start,goal)

'''

'''
def dfs(graph,start,goal):
    visited=set()
    path=[]

    def rec_dfs(current):
        visited.add(current)
        path.append(current)

        if current ==goal:
            return True

        for neighbour in graph[current]:
            if neighbour not in visited:
                if rec_dfs(neighbour):
                    return True


        path.pop()
        return False


    rec_dfs(start)
    return path
'''
graph={
    'A':['B','C'],
    'B':['D','E'],
    'D':['H','I'],
    'C':['G','F'],
    'F':['K'],
    'H':[],
    'I':[],
    'K':[],
    'G':[],
    'E':[]
}

start='A'
goal="G"
#print(dfs(graph,start,goal))


def dfs(graph,start,goal):
    visited=set()
    path=[]

    def rec_dfs(curr):
        visited.add(curr)
        path.append(curr)

        if curr==goal:
            return True

        for neighbour in graph[curr]:
            if neighbour is not visited:
                if rec_dfs(neighbour):
                    return True

        path.pop()
        return False
    rec_dfs(start)
    return path


print(dfs(graph,start,goal))
