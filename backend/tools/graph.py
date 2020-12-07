import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import time
import random


def plot(graph, backbone, isp, clients, bandwidth):
    pos = graphviz_layout(graph, prog="neato", args="")
    plt.figure(figsize=(8, 8))
    nx.draw_networkx_nodes(graph, pos, nodelist=isp, node_color="cyan")
    nx.draw_networkx_nodes(graph, pos, nodelist=backbone, node_color="red")
    nx.draw_networkx_nodes(graph, pos, nodelist=clients, node_color="green")
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(graph, pos, dict(enumerate(bandwidth)), font_size=12)
    plt.show()


def generate(num_nodes, num_backbone, m, q, p, min_clients, max_clients, min_isp_bandwidth, max_isp_bandwidth, min_client_bandwidth, max_client_bandwidth):
    random.seed(time.time())
    graph = nx.extended_barabasi_albert_graph(num_nodes, m, q, p, int(time.time()))
    while not nx.is_connected(graph):
        graph = nx.extended_barabasi_albert_graph(num_nodes, m, q, p, int(time.time()))
    bandwidth = [str(random.randint(min_isp_bandwidth, max_isp_bandwidth)) for _ in range(num_nodes)]
    backbone = [x + num_nodes for x in range(num_backbone)]
    backbone_connectors = []
    graph.add_nodes_from(backbone)
    for b in backbone:
        x = random.randint(0, num_nodes-1)
        graph.add_edge(b, x)
        backbone_connectors.append(x)
        bandwidth.append('')

    last = num_nodes + num_backbone
    client_nodes = []
    for x in range(num_nodes):
        if x not in backbone_connectors:
            clients = random.randint(min_clients, max_clients)
            for _ in range(clients):
                graph.add_node(last)
                graph.add_edge(x, last)
                client_nodes.append(last)
                bandwidth.append(str(random.randint(min_client_bandwidth, max_client_bandwidth)))
                last += 1

    # plot(graph, backbone, graph.nodes, client_nodes, bandwidth)
    return graph, backbone, graph.nodes, client_nodes, bandwidth

