"""3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, 
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""

import collections

def apvs(graph, start):
    Y, X = set(), collections.deque([start])
    Y.add(start)
    while X:
        start = X.popleft()
        for next in graph[start]:
            if next not in Y:
                Y.add(next)
                X.append(next)
        print(start)

def graphs(num):
    if num < 2:
        print('Слишком мало вершин')
        return
    graph = []
    for i in range(num):
        for j in range(num):
            if i != j:
                graph.append((i, j))
    list_graph = {}
    for i in graph:
        list_graph[str(i[0])] = [].append(str(i[1]))
    return list_graph


graph = {'0': set(['1', '2']),
        '1': set(['0', '3', '4']),
        '2': set(['0']),
        '3': set(['1']),
        '4': set(['2', '3'])}
#apvs(graph,'0')
graphs(int(input('Сколько друзей встретились: ')))