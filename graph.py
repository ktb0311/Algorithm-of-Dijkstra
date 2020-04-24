from Algorithm_of_Dijkstra import find_lowest_cost

graph = {'start':{},
             'a':{},
             'b':{},
             'c':{},
            'fin':None}

graph['start']['a'] = 10
graph['start']['c'] = 0
graph['a']['b'] = 20
graph['b']['c'] = 1
graph['b']['fin'] = 30
graph['c']['a'] = 50

result = find_lowest_cost(graph)
print(result)

graph = {'start':{}, 
         'a':{},
         'b':{},
         'c':{},
         'd':{},
         'fin':None}
graph['start']['a'] = 5
graph['start']['b'] = 0
graph['a']['d'] = 15
graph['a']['c'] = 20
graph['a']['b'] = -7
graph['b']['c'] = 35
graph['b']['d'] = 30
graph['c']['fin'] = 10
graph['d']['fin'] = 20

result = find_lowest_cost(graph)
print(result)