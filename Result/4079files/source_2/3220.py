from collections import namedtuple


def get_bottom_padding(height, d, num_nodes, base_y, y_offset):
    return base_y + height / 2 - ((num_nodes * d + (num_nodes - 1) * y_offset) / 2)


class TreeTraverse(object):
    def __init__(self):
        self.nodes = []
        self.edges = []

    def get_nodes_and_edges(self, model, attribute=None, value=None, parent=None, layer=1):
        Node = namedtuple('Node', ['num', 'attribute', 'value', 'output'])
        Edge = namedtuple('Edge', ['a', 'b'])

        node_num = len(self.nodes) + 1

        if value is not None:
            self.edges.append(Edge(a=parent, b=node_num))

        if model[0] == -1:
            self.nodes.append(Node(num=node_num, attribute=None, value=value, output=str(model[1])))
            return
        else:
            self.nodes.append(Node(num=node_num, attribute=model[0], value=value, output=None))
            for i, sub_model in enumerate(model[1:]):
                self.get_nodes_and_edges(model=sub_model, attribute=str(sub_model[0]), value=i, parent=node_num, layer=layer+1)

        return self.nodes, self.edges
