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
dot = Digraph(comment='The Round Table') 
adj=defaultdict(list)
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
def clicked2():
    a=txt.get()
    b=txt1.get()
    adj[a].append(b)
    window.destroy()
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
print(dot.source)  
dot.render('round-table.gv', view=True)       
#im = Image(G.create_png())
#display(im)
