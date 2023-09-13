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

This code defines a `DAG` class that represents a directed acyclic graph. The `add_node()` and `add_edge()` methods add a node and an edge to the graph, respectively. The `topological_sort()` method performs a topological sort of the graph, which is a linear ordering of the nodes such that no node precedes a node that depends on it.

The main function creates a **DAG** with four nodes and three edges. It then calls the `topological_sort()` method to print the topological order of the nodes.

> This is just an example. as always: not use in product!

---

## Use cases of _directed acyclic graphs_ (DAGs):

* **Data processing workflows:**\
DAGs can be used to represent the steps involved in processing a large dataset. The nodes in the DAG represent the different tasks that need to be performed, and the edges represent the dependencies between the tasks. This can be used to ensure that the data is processed in the correct order and that no tasks are skipped.
* **Build pipelines:**\
DAGs can be used to represent the steps involved in building a software product. The nodes in the DAG represent the different tasks that need to be performed, such as writing code, compiling code, and testing code. The edges represent the dependencies between the tasks. This can be used to ensure that the software product is built in the correct order and that no steps are skipped.
* **Machine learning workflows:**\
DAGs can be used to represent the steps involved in training and deploying a machine learning model. The nodes in the DAG represent the different tasks that need to be performed, such as data preparation, model training, and model evaluation. The edges represent the dependencies between the tasks. This can be used to ensure that the machine learning model is trained and deployed in the correct order.
* **Scheduling tasks:**\
DAGs can be used to schedule the execution of tasks. The nodes in the DAG represent the tasks that need to be executed, and the edges represent the dependencies between the tasks. This can be used to ensure that the tasks are executed in the correct order and that no tasks are missed.
* **Representing workflows:**\
DAGs can be used to represent any workflow that involves a sequence of tasks. This could include workflows for manufacturing, logistics, or healthcare.

* **Version control systems:**\
DAGs can be used to represent the history of changes to a codebase. This can be used to track changes to the code, identify conflicts, and revert to previous versions of the code.
* **Compilers:**\
DAGs can be used to represent the syntax tree of a program. This can be used to analyze the program, generate code, and optimize the code.
* **Network routing:**\
DAGs can be used to represent the routing tables of a network. This can be used to route traffic between different nodes in the network.
* **Scheduling algorithms:**\
DAGs can be used to schedule the execution of tasks on a computer or a network. This can be used to improve the performance of the system.

DAGs are a versatile data structure that can be used to solve a wide variety of problems.\
As the need for complex workflows continues to grow, DAGs are likely to become even more widely used.
