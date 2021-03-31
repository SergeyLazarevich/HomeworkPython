"""3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, 
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""

def apvs(graph, start):
    Y = set() 
    X = [start]
    Z = []
    Y.add(start)
    while X:
        Z.append(X.pop(0))
        for next in graph[start]:
            if next not in Y:
                Y.add(next)
                X.append(next)
    return Z

def graphs(num):
    if num < 2:
        print('Слишком мало вершин')
        return {'0':'0'}
    graph = {i:{j for j in range(num) if i != j} for i in range(num)}
    return graph

n = int(input('Введите кличество вершин: '))
number = int(input('С какой вершины вести счёт: '))
print('Граф в виде списка смежности:')
graph = graphs(n)
#print(graph)
for key, valume in graph.items():
    print(f'{key} : {valume}')
print('Путь в глубину:')
print(apvs(graph,number))

