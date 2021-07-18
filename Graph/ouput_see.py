from Graph import Graph

d={ 'A':['B','F','G'],
            'B':['C','D'],
            'C':[],
            'F':[],
            'G':['H'],
            'H':[],
            'D':['E'],
            'E':[]           }
g=Graph(d,name="My Graph")
bfs_result=g.bfs("A")
dfs_result=g.dfs("A")
g.gprint()
print(f"The Breadth First Search on the graph yields: {bfs_result}",end="\n\n")
print(f"The Depth First Search on the graph yields: {dfs_result}")