# quick-graph

Quickly visualize JSON graphs

## Usage

### Desired
```bash
$ python3 -m graph ./path/to/graph.json
# browser opens, revealing interactive network graph
```

### Current
```bash
$ python3 -m src.example
generating data
Wrote node-link JSON data to ./src/web/graph.json
waiting a second to start web browser
starting flask application
 * Serving Flask app 'example' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
127.0.0.1 - - [13/May/2021 22:04:17] "GET / HTTP/1.1" 304 -
127.0.0.1 - - [13/May/2021 22:04:17] "GET /web/graph.css HTTP/1.1" 304 -
127.0.0.1 - - [13/May/2021 22:04:17] "GET /web/graph.js HTTP/1.1" 304 -
127.0.0.1 - - [13/May/2021 22:04:17] "GET /web/graph.json HTTP/1.1" 200 -
```

## Ideas
Since my network graph JSON always have unique key names, it would be interesting to intuit the graph structure.

In other words, it would view the following two networks as equivalent
```
{"nodes": {"1": {"name": "Joe"}, "2": {"name": "Bill"}}, "edges": [{"from": "1", "to": "2"}]}
```
and
```
{"nodes": [{"id": "1", "name": "Joe"}, {"id": "2", "name": "Bill"}], "links": [{"src": "1", "dest": "2"}]}
```


