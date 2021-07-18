"""
Alternate Method

self.node=Node(n)
        
        while True:

            c=input(f"Press any key to continue else press n to stop entering Adjacency list values for {n}: ")
            if c.lower()=='n':
                break
            
            i=input(f"Enter Adjacency List Value for {n}: ")
            self.node.adjacent_list.append(self.inputer(i))   
        print(self.node.name,"===>",self.node.adjacent_list)
"""
"""
else:

            while True:
                node_Temp=input("Enter node of the graph: ")
                self.node_list.append(Node(node_Temp))

                c=input(f"Press any key to continue else press n to stop entering Nodes: ")
                if c.lower()=='n':
                    break

            for i in self.node_list:

                while True:

                    c=input(f"Press any key to continue else press n to stop entering Adjacency List for {i.name} : ")
                    if c.lower()=='n':
                        break

                    adjacency_list_Temp=input(f"Enter the adjacency list for the Node {i.name}: ")
                    for j in self.node_list:
                        if adjacency_list_Temp == j.name:
                            i.adjacent_list.append(j)


#d={'A':['B','C'],'B':[],'C':[]}                        
#a=Graph(d,name='A')
#a.print()
"""