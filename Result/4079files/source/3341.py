# Undirected non-weighted graph
import random
class graph:
    def __init__(self):
        self.vertices = {}
    def add_node(self,myid):
        if myid in self.vertices:
            print("Node already added")
        else:
            self.vertices[myid] = set()
    def add_edge(self,id1,id2):
        self.vertices[id1].add(id2)
    def show_graph(self):
        for key in self.vertices:
            print(str(key)+" : " + str(self.vertices[key]))
    def dfs(self,root):
        stack = [root]
        visited = set()
        seq = []
        while stack:
            curr = stack.pop()
            if curr not in visited:
                seq.append(curr)
                visited.add(curr)
                stack.extend(self.vertices[curr] - visited)
        return seq
    def bfs(self,root):
        queue = [root]
        visited = set()
        seq = []
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                seq.append(curr)
                visited.add(curr)
                queue.extend(self.vertices[curr] - visited)
        return seq
    def check_bipartite(self):
        all_vertices = self.vertices.keys()
        root = random.choice(list(all_vertices))
        colors = {}
        for key in all_vertices:
            colors[key] = -1
        colors[root] = 0
        queue = [root]
        visited = set()
        while queue:
            curr = queue.pop(0)

            curr_color = colors[curr]
            new_color = (curr_color+1)%2
            adjs = self.vertices[curr]
            visited.add(curr)
            for adj in adjs:
                if colors[adj]!=-1 and colors[adj]!=new_color:
                    return False
                else:
                    colors[adj] = new_color
            queue.extend(adjs - visited)
        return True
    # def shortest_path(start,end):
    #     queue = [start , [start]]
    #     visited = set()
    #     while queue:
    #         curr , curr_path = queue.pop(0)
    #         for next in self.vertices

g = graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_edge(1,4)
g.add_edge(1,3)
g.add_edge(3,2)
g.add_edge(4,3)
print(g.check_bipartite())
