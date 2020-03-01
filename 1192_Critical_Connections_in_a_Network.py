from typing import *

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for src,tgt in connections:
            graph[src].append(tgt)
            graph[tgt].append(src)

        ranks = {node: -2 for node in graph}

        edges = set()
        for connection in connections:
            edges.add(tuple(connection))
            edges.add(tuple(connection[::-1]))

        def dfs(node,rank):
            if(ranks[node]>=0):
                return ranks[node]

            nodesToVisit = graph[node]
            ranks[node] = rank
            newRank =  rank
            for tgtNode in nodesToVisit:
                if (rank-ranks[tgtNode]) == 1:
                    continue

                tgtNodeRank = dfs(tgtNode,rank+1)
                newRank = min(tgtNodeRank,newRank)
                if tgtNodeRank <= rank:
                    edges.remove((node,tgtNode))
                    edges.remove((tgtNode,node))

            return newRank

        for node in graph:
            dfs(node,0)

        edges = set(map(tuple,map(sorted,edges)))

        return edges

assert(Solution.criticalConnections(4,[[]]) == [])
assert(Solution.criticalConnections(4,[[0,1],[1,2],[2,0],[1,3]]) == [[1,3]])
assert(Solution.criticalConnections(3,[[0,1],[1,2],[2,3]]) == [[0,1],[1,2],[2,3]])