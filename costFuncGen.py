import networkx as nx

def adder_cost(graph,idx):

    pass
def print_cost_function(graph):
    pass

def print_node(graph,idx):
    print idx,graph.node[idx]
def cost(graph,idx):
    plist=graph.predecessors(idx)
    if(plist==0):
        pass
    elif(plist==1):
        pass
    elif(plist==2):
        pass
    else:
        print "Error: ", graph.node[idx]

def cost_func(graph, idx):

    plist=graph.predecessors(idx):

def bfs(graph,func):
    queue=['0'];
    for idx in graph.nodes():
        graph.node[idx]['color']=False;
    while(len(queue)!=0):
        head=queue[0]
        queue.pop(0);
        if(graph.node[head]['color']==False):
            graph.node[head]['color']=True;
            func(graph,head)
        else:
            continue
        for idx in graph.successors(head):
            if(graph.node[idx]['color']==False):
                queue.append(idx);


if __name__=="__main__":
    g=nx.read_dot('test_graph.dot')
    bfs(g,print_node)
