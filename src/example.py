import json
from threading import Timer
import webbrowser

import flask
import networkx as nx
from networkx.readwrite import json_graph


def generate_data(destination_filepath: str):
    G = nx.barbell_graph(6, 3)
    # this d3 example uses the name attribute for the mouse-hover value,
    # so add a name to each node
    for n in G:
        G.nodes[n]["name"] = n
    # write json formatted data
    d = json_graph.node_link_data(G)  # node-link format to serialize
    # write json
    json.dump(d, open(destination_filepath, "w"))
    print(f"Wrote node-link JSON data to {destination_filepath}")


# Serve the file over http to allow for cross origin requests
app = flask.Flask(__name__, static_folder="web")


@app.route("/")
def static_proxy():
    return app.send_static_file("graph.html")


def open_browser():
    webbrowser.open_new('http://localhost:8000/')


if __name__ == '__main__':
    print("generating data")
    generate_data("./src/web/graph.json")
    print("waiting a second to start web browser")
    Timer(1, open_browser).start();
    print("starting flask application")
    app.run(port=8000)

