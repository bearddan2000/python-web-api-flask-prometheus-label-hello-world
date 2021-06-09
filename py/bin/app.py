from flask import Flask, jsonify
from prometheus_client import Counter

view_metric = Counter('view', 'Product view', ['greeting'])

app = Flask(__name__)

@app.route('/')
def hello():
    msg = {"message": "hello world"}
    view_metric.labels(greeting="en").inc()
    return jsonify(msg)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
