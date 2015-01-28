import networkx as nx

def adder_cost(graph,idx):
    plist=graph.predecessors(idx);
    if(len(plist)==2):
        args='({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}{})'\
        .format(
        graph.node[plist[0]]['E']  ,
        graph.node[plist[0]]['V']  ,
        graph.node[plist[0]]['NE'] ,
        graph.node[plist[0]]['NV'] ,
        graph.node[plist[0]]['COV'],
        graph.node[plist[1]]['E']  ,
        graph.node[plist[1]]['V']  ,
        graph.node[plist[1]]['NE'] ,
        graph.node[plist[1]]['NV'] ,
        graph.node[plist[1]]['COV'],
        graph.node[idx]['NAME'],'_FBITS'
        )
        graph.node[idx]['NE']='E_ADD({})'.format(args)
        graph.node[idx]['NV']='V_ADD({})'.format(args)
        graph.node[idx]['COV']='C_ADD({})'.format(args)
    else:
        print 'Error,',graph.node[idx]

def mult_cost(graph,idx):
    plist=graph.predecessors(idx);
    print plist, graph.node['6']
    if(len(plist)==2):
        args='({}, {}, {}, {}, {}, {}, {}, {}, {}, {},  {}{}, {}{})'\
        .format(
        graph.node[plist[0]]['E']  ,
        graph.node[plist[0]]['V']  ,
        graph.node[plist[0]]['NE'] ,
        graph.node[plist[0]]['NV'] ,
        graph.node[plist[0]]['COV'],
        graph.node[plist[1]]['E']  ,
        graph.node[plist[1]]['V']  ,
        graph.node[plist[1]]['NE'] ,
        graph.node[plist[1]]['NV'] ,
        graph.node[plist[1]]['COV'],
        graph.node[idx]['NAME'],'_L_FBITS',
        graph.node[idx]['NAME'],'_R_FBITS'
        )
        graph.node[idx]['NE']='E_ADD({})'.format(args)
        graph.node[idx]['NV']='V_ADD({})'.format(args)
        graph.node[idx]['COV']='C_ADD({})'.format(args)
    else:
        print 'Error,',graph.node[idx]

def data_cost(graph,idx):
    plist=graph.predecessors(idx)
    if(len(plist)==1):
        if('0' in plist):
            graph.node[idx]['NE']='0'
            graph.node[idx]['NV']='0'
            graph.node[idx]['COV']='0'
        else:
            print graph.node[plist[0]],idx,plist
            graph.node[idx]['NE']=graph.node[plist[0]]['NE']
            graph.node[idx]['NV']=graph.node[plist[0]]['NV']
            graph.node[idx]['COV']=graph.node[plist[0]]['COV']
    else:
        print 'Error: not support yet'


def print_cost_function(graph):
    pass

def print_node(graph,idx):
    print idx,graph.node[idx]
def cost(graph,idx):
    plist=graph.predecessors(idx)
    if(len(plist)==0):
        pass
    elif(len(plist)==1):
        pass
    elif(len(plist)==2):
        pass
    else:
        print "Error: ", graph.node[idx]

def cost_func(graph, idx):
    if(graph.node[idx]['OP']=='add'):
        adder_cost(graph,idx)
    elif(graph.node[idx]['OP']=='cmul'):
        mult_cost(graph,idx)
    elif(graph.node[idx]['OP']=='data'):
        data_cost(graph,idx)
    elif(graph.node[idx]['OP']=='const'):
        data_cost(graph,idx)
    else:
        print graph.node[idx]

def bfs(graph,func):
    queue=['0'];
    for idx in graph.nodes():
        graph.node[idx]['color']=False;
    while(len(queue)!=0):
        head=queue[0]
        queue.pop(0);
        if(graph.node[head]['color']==False):
            graph.node[head]['color']=True;
            print head
            cost_func(graph,head)
        else:
            continue
        for idx in graph.successors(head):
            if(graph.node[idx]['color']==False):
                queue.append(idx);


if __name__=="__main__":
    g=nx.read_dot('test_graph.dot')
    bfs(g,print_node)

    print g.node['13']
