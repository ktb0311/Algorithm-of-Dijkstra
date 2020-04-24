def find_lowest_cost(graph, start = 'start', fin = 'fin'):      #Graph - сам граф, start - начальный узел, fin - конечный узел.
    print('GRAPH:',graph,'START =',start, 'FINISH =',fin)

    def create_costs():
        costs = {}
        for node in graph:
            if node == start:
                costs = {node:graph[start][node] for node in graph[start]} #Генерируем значения для начальных узлов т.е. cоседей start
            if node not in costs:                                           
                costs[node] = infinity                          #Остальным присваиваем infinity
        print('COSTS:', costs)
        return costs
    
    def create_parents():
        parents = {node:None for node in graph}                 #Генерируем таблицу(словарь) для родителя узла
        print('PARENTS:',parents)
        return parents

    def find_lowest_cost_node():                                #Узел с низкой стоимостью
        lowest_cost = infinity
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]                                  #Стоимость из таблицы
            if cost < lowest_cost and node not in processed:    #Если стоимость ниже и его нет в обработанных.
                lowest_cost = cost
                lowest_cost_node = node
        print('LOWEST COST =', lowest_cost)
        print('LOWEST COST NODE =', lowest_cost_node)
        return lowest_cost_node

    infinity = float('inf')         #Положительное бесконечное число
    
    processed = []                  #Список обработанных узлов. Нужен чтобы не было повторения
    parents = create_parents()      #Таблица(словарь) родителей узлов с низкой стоимостью
    costs = create_costs()          #Таблица(словарь) со стоимостью каждого узла

    node = find_lowest_cost_node()      #Узел с низкой стоимостью
    
    while graph[node] is not None:      #Выполнять пока у узла есть соседи
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node()
    lowest_cost = costs[node]
    return lowest_cost

if __name__ == '__main__':      #Если запущен сам файл
    graph = {'start':{}, 
             'a':{},
             'b':{},
             'c':{},
             'd':{},
             'fin':None}
    graph['start']['a'] = 5
    graph['start']['b'] = 2
    graph['a']['d'] = 2
    graph['a']['c'] = 4
    graph['b']['a'] = 8
    graph['b']['d'] = 7
    graph['c']['fin'] = 3
    graph['c']['d'] = 6
    graph['d']['fin'] = 1

    result = find_lowest_cost(graph)
    print(result)