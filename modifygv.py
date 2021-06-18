''' GRAPHVIZ COLORMAP '''

import graphviz
import os, sys

S0 = 'digraph G{graph [size = "30, 20", overlap = "scale"]'
S1 = '\nnode [style="filled" , colorscheme=prgn5]'

def load_file(file_name): #to load a file for viewing or modifying
    file_alter = graphviz.Source.from_file(file_name)
    return file_alter

def set_map(stri_name, node): # to modify the gv file and insert colour map for eg.. set_map(x,y), x is gvfile and y is heatmap for nodes!
    tmp = stri_name.source
    tmp = tmp.split(";")
    tmp[0] = S0
    tmp[1] = S1
    for i in range(3, len(node)):
        tmp[i+3] = "{} [{} = {}]".format(tmp[i+3],"color", int(node[i]/20))
    new_sent = ";".join(map(str,tmp))
    return new_sent
    
def save_file(file_name, stri_name): # to save the modified file to gv
    with open(file_name, "w") as out:
        out.write(stri_name)
        
def view(stri_name, ngin = "neato", form = "png"):  #to view the file in neato in the png format      
    stri_name.engine = ngin
    stri_name.format = form
    stri_name.view()
    
    
def main(file_name, node, file_sn):
    a = load_file(file_name)
    b = set_map(a, node)
    save_file(file_sn, b)
    
