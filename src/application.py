from flask import Flask, Response, request
from datetime import datetime
import json
from shopping_resource import ShoppingResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)

CORS(app)

@app.route("/api/carts", methods=["GET"])
def get_all_carts():

    size = request.args.get('size', 20)
    result = ShoppingResource.get_carts(int(size))

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/carts_id/<id>", methods=["GET"])
def get_carts_by_id(id):

    result = ShoppingResource.get_by_key(id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/items", methods=["GET"])
def get_items():

    size = request.args.get('size', 20)
    result = ShoppingResource.get_items(int(size))

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/items_id/<item_id>", methods=["GET"])
def get_items_by_id(item_id):

    result = ShoppingResource.get_by_item_id(item_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/items_name/<name>", methods=["GET"])
def get_items_by_name(name):

    size = request.args.get('size', 20)
    result = ShoppingResource.get_by_item_name(name, size)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/items/create", methods=["POST"])
def create_item():

    request_json = request.get_json()
    item_id = request_json.get('item_id')
    name = request_json.get('item_name')
    description = request_json.get('description')
    result = ShoppingResource.create_item(item_id, description, name)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("ITEM NOT CREATED", status=404, content_type="text/plain")

    return rsp


@app.route("/api/carts/create", methods=["POST"])
def create_cart():
    request_json = request.get_json()
    user_id = request_json.get('user_id')
    cart_id = request_json.get('cart_id')
    result = ShoppingResource.create_cart(user_id, cart_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("CART NOT CREATED", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

