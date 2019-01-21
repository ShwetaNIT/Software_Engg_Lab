# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 23:12:02 2019

@author: Shweta
"""
from collections import defaultdict
from IPython.display import Image, display
import pydot
from graphviz import Digraph


from tkinter import *
from tkinter import messagebox
#import Tkinter
#import tkMessageBox


#This class represents a directed graph  
# using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        #No. of vertices 
        self.V= vertices  
          
        # default dictionary to store graph 
        self.graph = defaultdict(list)  
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path): 
  
        # Mark the current node as visited and store in path 
        visited[u]= True
        path.append(u) 
  
        # If current vertex is same as destination, then print 
        # current path[] 
        if u ==d: 
            print(path) 
        else: 
            # If current vertex is not destination 
            #Recur for all the vertices adjacent to this vertex 
            for i in self.graph[u]: 
                if visited[i]==False: 
                    self.printAllPathsUtil(i, d, visited, path) 
                      
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False
   
   
    # Prints all paths from 's' to 'd' 
    def printAllPaths(self,s, d): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
  
        # Create an array to store paths 
        path = [] 
  
        # Call the recursive helper function to print all paths 
        self.printAllPathsUtil(s, d,visited, path) 
   



dot = Digraph(comment='The Round Table') 
adj=defaultdict(list)
node=set()
edges=0
nodes=0
window = Tk()
 
window.title("Graph Specifications")
 
window.geometry('300x75')
 
lbl = Label(window, text="Starting Node")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=30)
 
txt.grid(column=1, row=0)

lbl1 = Label(window, text="Ending Node")
 
lbl1.grid(column=0, row=1)
 
txt1 = Entry(window,width=30)
 
txt1.grid(column=1, row=1)

def clicked1():
    a=txt.get()
    b=txt1.get()
    adj[a].append(b)
    txt.delete(first=0,last=10)
    txt1.delete(first=0,last=10)
    #edges=edges+1
def clicked2():
    a=txt.get()
    b=txt1.get()
    adj[a].append(b)
    window.destroy()
    #edges=edges+1
btn1 = Button(window, text="Next", command=clicked1)
btn2 = Button(window, text="Over", command=clicked2) 
btn1.grid(column=0, row=2)
btn2.grid(column=1, row=2) 
window.mainloop()
#G = pydot.Dot(graph_type="digraph")  
    
for i in adj.keys():
    dot.node(str(i))
    
    #G.add_node(node)
 
for i in adj.keys():
    for j in adj[i]:
       # edge = pydot.Edge(i,j)
        dot.edge(str(i),str(j))
        edges=edges+1
        node.add(i)
        node.add(j)
       

maxi=0
for i in node:
    nodes=nodes+1
    if int(i)>maxi:
        maxi=int(i)
g = Graph(nodes) 
print(edges-nodes+1)

for i in adj.keys():
    for j in adj[i]:
       # edge = pydot.Edge(i,j)
        g.addEdge(int(i),int(j))
        

print(dot.source)  
dot.render('round-table.gv', view=True)       
#im = Image(G.create_png())
#display(im)

top = Tk()
def hello():
   messagebox.showinfo("No of Regions",str(edges-nodes+1))
def hello1():
    top.destroy()
B1 = Button(top, text = "CLick for bounded regions", command = hello)
B2=  Button(top, text = "Exit", command = hello1)
B1.pack()
B2.pack()

top.mainloop()


s=0
d=maxi
print ("Following are all different paths from %d to %d :" %(s, d)) 
g.printAllPaths(s, d) 

