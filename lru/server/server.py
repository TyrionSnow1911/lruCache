import os
import json
import argparse
from lru.server.lru import LRUCache

# from flask_cors import CORS
from flask import Flask, request, jsonify


app = Flask(__name__)
# CORS(app)


def setLruSize(size):
    global lruCache
    lruCache = LRUCache(size)


@app.route("/get/:key", methods=["GET"])
def get():
    key = request.args.get("key")
    result = lruCache.get(key)
    return json.dumps({"success": True, "data": result}), 200


@app.route("/put", methods=["PUT"])
def put():
    key = request.args.get("key")
    value = request.args.get("value")
    lruCache.put(key, value)
    return json.dumps({"success": True}), 200


@app.route("/delete", methods=["DELETE"])
def delete():
    key = request.args.get("key")
    lruCache.delete(key)
    return json.dumps({"success": True}), 200


@app.route("/reset", methods=["POST"])
def reset():
    lruCache.reset()
    return json.dumps({"success": True}), 200


if __name__ == "__main__":
    lruCache = None
    parser = argparse.ArgumentParser(description="Valhalla trading application")

    parser.add_argument(
        "-s",
        "--size",
        help="lru max size; \
                Tells the app the maximum size to initialize LRU cache with.",
    )

    args = vars(parser.parse_args())
    size = args["size"]

    setLruSize(size)

    app.run(host="localhost", port=8080, debug=True)
