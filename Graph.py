from networkx import all_shortest_paths, exception, DiGraph
from csv import reader as read
##This file contains function to get the list of all shortests
##ways between two pals
##
##It uses breed.csv and return a list of png paths

#function to get a dict with pals and their childrens
def getCsvContent(file : str):
    pals={}
    with open(file, 'r',encoding='utf-8') as f:
        reader = read(f,delimiter=',')
        for row in reader:
            pals[row[0]]=row[1:]
    return pals

#function to get the graph of all the pals and their relations
def getPalsGraph(csvContent : dict):
    G = DiGraph()
    for parent, enfants in csvContent.items():
        for enfant in enfants:
            G.add_edge(parent, enfant)
    return G

#function to get all the parents of a child
def findParents(pal : str, enfant : str):
    secondParents=[]
    childrens=getCsvContent("data.csv")[pal]
    palList=[]
    with open("data.csv", 'r',encoding='utf-8') as f:
        reader = read(f,delimiter=',')
        for row in reader:
            palList.append(row[0])
    for childrenIndex in range(len(childrens)):
        if childrens[childrenIndex]==enfant:
            secondParents.append(palList[childrenIndex])
    return secondParents

#function to get the shorstests ways between a parent and a child
def getShortestWays(parent : str, child : str):
    if(parent=="Select a parent" or child=="Select a child"):
        return []
    if(child in getCsvContent("data.csv")[parent]):
        return [[parent,child]]
    else:
        try :
            return list(all_shortest_paths(getPalsGraph(getCsvContent("data.csv")),parent,child))
        except exception.NetworkXNoPath:
            return []

def getJSONShortestWays(parent : str, child : str):
    ways=getShortestWays(parent,child)
    waysJSON={}
    index=0
    for way in ways:
        waysJSON["way"+str(index)]=way
        index+=1
    return waysJSON