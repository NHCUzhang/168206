def TopoSort(graph):
    in_degrees = dict((u,0) for u in graph)  #初始化所有顶点入度为0
    vertex_num = len(in_degrees)	
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1  #计算每个顶点的入度
			
    D = [u for u in in_degrees if in_degrees[u] == 0]  # 筛选入度为0的顶点
    result = []
    while D:
        u = D.pop()  #默认从最后一个删除
        result.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1  #移除其所有指向
            if in_degrees[v] == 0:
                D.append(v)     #再次筛选入度为0的顶点
				
    if len(result) == vertex_num:  #如果循环结束后存在非0入度的顶点说明图中有环
        return result
    else:
        print("There are circuit.")
		
G = {
    'a':'bce',
    'b':'d',
    'c':'d',
    'd':'e',
    'e':'cd'
}
print(TopoSort(G))
