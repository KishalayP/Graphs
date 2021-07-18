class Node():

    def __init__(self,name):
        self.name = name
        self.adjacent_list=[]
        self.visited=False
        self.predecessor=None


class Graph():

    def __init__(self,dic,name="Graph 1"):
        self.gphname=name
        self.node_list=[]
        self.node_adj_list=[]
        self.dic=dic
   
        for i in self.dic:
            self.node_list.append(Node(i))

        for i in self.node_list:

            adjacency_list_Temp=self.dic.get(i.name)
            for j in self.node_list:
                if j.name in adjacency_list_Temp:
                    i.adjacent_list.append(j)

    
    def gprint(self):
        print(f"\nX-----------------------{self.gphname}-------------------------X")
        print(f"\nNo of Nodes in graph is {len(self.node_list)}",end="\n\n")
        for i in self.node_list:
            l=[]
            print(f"Node Value is: {i.name}")
            print(f"Nodes in Adjacency list for {i.name}: ",end="")
            if i.adjacent_list:
                for j in i.adjacent_list:
                    l.append(j.name)
                print(l,end="\n\n")
            else:
                print("None",end="\n\n")
        print(f"X-----------------------{self.gphname}-------------------------X\n")


    def bfs(self,start_node):

        for i in self.node_list:
            if start_node==i.name:
                self.start_node=i
        queue=[]
        ll=[]
        queue.append(self.start_node)
        self.start_node.visited=True
        while queue:

            actual_node=queue.pop(0)
            #print(f"{actual_node.name}",end="\n")
            ll.append(actual_node.name)

            for i in actual_node.adjacent_list:
                if not i.visited:
                    i.visited=True
                    queue.append(i)

        for i in self.node_list:
            i.visited=False
        return ll


    def dfs(self,start_bnoder):

        for i in self.node_list:
            if start_bnoder==i.name:
                self.start_bnoder=i
                break
 
        stack=[]
        self.l2=[]
        stack.append(self.start_bnoder)
        self.start_bnoder.visited=True

        while stack: 

            current_node=stack.pop() 
            
            self.l2.append(current_node.name)

            for i in reversed(current_node.adjacent_list):
                if not i.visited:
                    i.visited=True
                    stack.append(i)
        
        for i in self.node_list:
            i.visited=False
                    
        return self.l2
        

    l2=[]
    def dfs_recursion(self,start_noder):

        for i in self.node_list:
            if isinstance(start_noder,Node):
                self.start_noder=start_noder
                break
            elif start_noder==i.name:
                self.start_noder=i
                break
            
        
        Graph.l2.append(self.start_noder.name)
        self.start_noder.visited=True
          
        for i in self.start_noder.adjacent_list:
            if not i.visited:
                self.dfs(i)
        return self.l2
