# cost function generator

import networkx as nx
class test_graph:
    def __init__(this):
        this.dot=nx.DiGraph();
        this.idx=2
        this.dot.add_node(0)
        this.dot.node[0]['name']='src'
        this.dot.add_node(1)
        this.dot.node[1]['name']='sink'
    def create_data_node(this,name,index,mean,var):
        idx=this.newNodeIdx();
        this.dot.add_node(idx);
        this.dot.node[idx]['name']=name;
        this.dot.node[idx]['idx']=index;
        this.dot.node[idx]['var']=var;
        this.dot.node[idx]['mean']=mean;
        return idx;

    def create_add_node(this,name,mean,var):
        idx=this.newNodeIdx();
        this.dot.add_node(idx);
        this.dot.node[idx]['OP']='add'
        this.dot.node[idx]['name']=name;
        this.dot.node[idx]['var']=var;
        this.dot.node[idx]['mean']=mean;
        this.dot.node[idx]['idx']=-1
        return idx;

    def create_cmul_node(this,name,mean,var):
        idx=this.newNodeIdx();
        this.dot.add_node(idx);
        this.dot.node[idx]['OP']='cmul'
        this.dot.node[idx]['name']=name;
        this.dot.node[idx]['var']=var;
        this.dot.node[idx]['mean']=mean;
        this.dot.node[idx]['idx']=-1
        return idx;

    def create_const_node(this,name,index,value):
        idx=this.newNodeIdx();
        this.dot.add_node(idx);
        this.dot.node[idx]['OP']='cmul'
        this.dot.node[idx]['name']=name;
        this.dot.node[idx]['var']=0;
        this.dot.node[idx]['mean']=value;
        this.dot.node[idx]['idx']=-1;
        return idx
    def newNodeIdx(this):
        ret=this.idx
        this.idx=this.idx+1
        return ret;
    def example0(this):
        # coeff= flaot coeff[3]={1.1,2.1,3.3}
        # data = float a[3] = {all, mean=0,var=4}
        # function dot_product(coeff,data)
        a=[this.create_data_node('a',0,0,4),
            this.create_data_node('a',1,0,4),
            this.create_data_node('a',2,0,4)]
        coeff=[this.create_const_node('coeff',1,1.1),
            this.create_const_node('coeff',1,2.1),
            this.create_const_node('coeff',2,3.3)]
        mul=[this.create_cmul_node('mul0',0,1.1*1.1),
            this.create_cmul_node('mul1',0,2.1*2.1),
            this.create_cmul_node('mul2',0,3.3*3.3)]
        add=[this.create_add_node('add0',0,1.1*1.1+2.1*2.2),
            this.create_add_node('add1',0,1.1*1.1+2.1*2.1+3.3*3.3)]
        out=this.create_data_node('s',0,0,1.1*1.1+2.1*2.1+3.3*3.3)
        print a
        print coeff
        print mul
        print add
        print out
        this.dot.add_edges_from(
            [(0,a[0]),
             (0,a[1]),
             (0,a[2]),
             (0,coeff[0]),
             (0,coeff[1]),
             (0,coeff[2]),
            (a[0],mul[0]),
            (a[1],mul[1]),
            (a[2],mul[2]),
            (coeff[0],mul[0]),
            (coeff[1],mul[1]),
            (coeff[2],mul[2]),
            (mul[0],add[0]),
            (mul[1],add[0]),
            (add[0],add[1]),
            (mul[2],add[1]),
            (add[1],out),
            (out,1)
            ])
    def save(this,filename=None):
        if(filename==None):
            filename='test_graph.dot'
        nx.write_dot(this.dot,filename)
#
# def ts_graph():
#     dot=nx.Graph();
#     dot.add_node(0)
#     dot.add_node(1)
#     dot.add_edge(0,1)
#     dot.node[0]['name'] ='a'
#     dot.node[0]['index']=0
#     dot.node[0]['var']  =1.0
#     dot.node[0]['mean'] =0.1
#     A=test_graph()
#     A.example0()
# return dot
import matplotlib.pyplot as plt
if __name__ == "__main__":
    # dot=ts_graph();
    A=test_graph()
    A.example0()
    A.save()
    g=nx.read_dot('test_graph.dot')
    print g.nodes()
