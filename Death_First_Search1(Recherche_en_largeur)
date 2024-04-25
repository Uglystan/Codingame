from queue import Queue
import time
import sys

def find_in_dict(node, value_search):
    for key, value in node.items():
        if value == value_search:
            return (key)
    return (None)

def shortest_way(pos, node, gateway_node):
    first = 0
    marque = []
    file_attente = Queue()

    file_attente.put(node[pos])

    while 1: #SI pas de solution
        first = file_attente.get()

        for i in first:
            if i in gateway_node:
                n = find_in_dict(node, first)
                node[n].remove(i)
                print(n, i)
                return

        for i in first:
            if i not in marque:
                file_attente.put(node[i])

        marque.append(first)




# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
node: dict[int, list[int]] = {}
gateway_node = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    if node.get(n1) == None:
        node[n1] = []
    node[n1].append(n2)
    node[n1].sort()
    if node.get(n2) == None:
        node[n2] = []
    node[n2].append(n1)
    node[n2].sort()

for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateway_node.append(ei)
# print(node, gateway_node)

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    t1 = time.time()
    shortest_way(si, node, gateway_node)
    t2 = time.time()
    d = (t2 - t1) * 1000
    print(d, file = sys.stderr)


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
