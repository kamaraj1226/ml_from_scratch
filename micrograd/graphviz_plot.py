"""
to plot neurons
"""

from graphviz import Digraph
import os


def trace(root):
    """
    For the given root node
    traverse through the node and returns all the edges and nodes
    """
    nodes, edges = set(), set()

    def build(v):
        if v in nodes:
            return

        nodes.add(v)
        for child in v.prev:
            edges.add((child, v))
            build(child)

    build(root)

    return nodes, edges


def draw_dot(root):
    """
    Takes the node and traverse the node and plot
    """
    # set graphviz
    os.environ["PATH"] = r"C:\Program Files\Graphviz\bin"

    dot = Digraph(format="svg", graph_attr={"rankdir": "LR"})

    nodes, edges = trace(root)

    for node in nodes:
        uid = str(id(node))

        dot.node(
            name=uid,
            label=f"{node.label} | data: {node.data:.4f} | grad: {node.grad:.4f}",
            shape="record",
        )

        if node.op:
            dot.node(name=uid + node.op, label=node.op)

            dot.edge(uid + node.op, uid)

    for n1, n2 in edges:
        _n1 = str(id(n1))
        _n2 = str(id(n2)) + n2.op

        dot.edge(_n1, _n2)

    return dot
