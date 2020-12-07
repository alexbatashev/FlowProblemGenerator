from flask import Flask
from backend.tools.graph import *
import networkx as nx
from flask import request


app = Flask(__name__)


@app.route('/')
def home():
    num_isp_nodes = int(request.args.get('num_isp_nodes'))
    num_backbone_nodes = int(request.args.get('num_backbone_nodes'))
    m = int(request.args.get('m'))
    p = float(request.args.get('p'))
    q = float(request.args.get('q'))
    min_clients = int(request.args.get('min_clients'))
    max_clients = int(request.args.get('max_clients'))
    min_isp_bandwidth = int(request.args.get('min_isp_bandwidth'))
    max_isp_bandwidth = int(request.args.get('max_isp_bandwidth'))
    min_client_bandwidth = int(request.args.get('min_client_bandwidth'))
    max_client_bandwidth = int(request.args.get('max_client_bandwidth'))
    graph, backbone, _, clients, bandwidth = generate(
        num_isp_nodes,
        num_backbone_nodes,
        m,
        p,
        q,
        min_clients,
        max_clients,
        min_isp_bandwidth,
        max_isp_bandwidth,
        min_client_bandwidth,
        max_client_bandwidth
    )
    struct = nx.node_link_data(graph)
    struct['backbone'] = backbone
    struct['clients'] = clients
    struct['bandwidth'] = bandwidth
    return struct
