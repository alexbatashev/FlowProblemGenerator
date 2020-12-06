from flask import Flask
from backend.tools.graph import *
import networkx as nx


app = Flask(__name__)


@app.route('/')
def home():
    graph, backbone, _, clients, _ = generate(8, 1, 2, 4, 10, 15, 40, 100, 20, 150)
    struct = nx.node_link_data(graph)
    struct['backbone'] = backbone
    struct['clients'] = clients
    return struct
