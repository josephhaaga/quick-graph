# quick-graph

Interactive visualization for NetworkX graphs.

## Usage

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

