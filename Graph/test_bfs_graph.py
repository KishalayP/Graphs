from unittest import TestCase
from Graph import Graph 

class bfs_Graph_Test(TestCase):

    def test_bfs_1(self):
        d={ 'A':['B','F','G'],
            'B':['C','D'],
            'C':[],
            'F':[],
            'G':['H'],
            'H':[],
            'D':['E'],
            'E':[],          }

        g=Graph(d)
        expec_result=['A','B','F','G','C','D','H','E']
        actual_result=g.bfs("A")
        self.assertListEqual(actual_result,expec_result)

    def test_bfs_2(self):
        d={ 'A':['B','C'],
            'B':['D'],
            'C':[],
            'D':['E'],
            'E':[]           }

        g=Graph(d)
        expec_result=['A','B','C','D','E']
        actual_result=g.bfs("A")
        self.assertListEqual(actual_result,expec_result)
        