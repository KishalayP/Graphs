from unittest import TestCase
from Graph import Graph 

class dfs_Graph_Test(TestCase):

    def test_dfs_1(self):
        d={ 'A':['B','F','G'],
            'B':['C','D'],
            'C':[],
            'F':[],
            'G':['H'],
            'H':[],
            'D':['E'],
            'E':[]           }

        g=Graph(d)
        expec_result=['A','B','C','D','E','F','G','H']
        actual_result=g.dfs("A")
        self.assertListEqual(actual_result,expec_result)

    def test_dfs_2(self):
        d={ 'A':['B','C'],
            'B':['D'],
            'C':[],
            'D':['E'],
            'E':[]           }

        g1=Graph(d)
        expec_result=['A','B','D','E','C']
        actual_result=g1.dfs("A")
        self.assertListEqual(actual_result,expec_result)
       

     

