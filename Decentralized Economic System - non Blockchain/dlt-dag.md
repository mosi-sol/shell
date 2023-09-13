## Directed Acyclic Graph (DAG):

```py
class DAG:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, start_node, end_node):
        self.edges.append((start_node, end_node))

    def topological_sort(self):
        """
        Performs a topological sort of the DAG.

        Returns:
            A list of nodes in topological order.
        """
        in_degree = {node: 0 for node in self.nodes}
        for start_node, end_node in self.edges:
            in_degree[end_node] += 1

        queue = []
        for node in self.nodes:
            if in_degree[node] == 0:
                queue.append(node)

        topological_order = []
        while queue:
            node = queue.pop(0)
            topological_order.append(node)

            for end_node in self.edges:
                if end_node[1] == node:
                    in_degree[end_node[0]] -= 1
                    if in_degree[end_node[0]] == 0:
                        queue.append(end_node[0])

        return topological_order


def main():
    dag = DAG()
    dag.add_node("A")
    dag.add_node("B")
    dag.add_node("C")
    dag.add_node("D")
    dag.add_edge("A", "B")
    dag.add_edge("B", "C")
    dag.add_edge("C", "D")

    print(dag.topological_sort())


if __name__ == "__main__":
    main()

```

This code defines a DAG class that represents a directed acyclic graph. The add_node() and add_edge() methods add a node and an edge to the graph, respectively. The topological_sort() method performs a topological sort of the graph, which is a linear ordering of the nodes such that no node precedes a node that depends on it.

The main function creates a DAG with four nodes and three edges. It then calls the topological_sort() method to print the topological order of the nodes.

> This is just an example. as always: not use in product!
