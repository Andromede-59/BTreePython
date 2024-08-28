from graphviz import Digraph

def draw_binary_tree(root):
    dot = Digraph(format='png')

    def add_nodes_edges(node, parent_name=None):
        if node is None:
            return
        node_name = str(id(node))
        dot.node(node_name, label=str(node.keys))
        if parent_name is not None:
            dot.edge(parent_name, node_name)
        for ch in node.children:
            add_nodes_edges(ch, node_name)

    add_nodes_edges(root)
    dot.render('binary_tree', view=True)