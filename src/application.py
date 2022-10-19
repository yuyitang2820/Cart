from flask import Flask, Response, request
from datetime import datetime
import json
from shopping_resource import ShoppingResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)

CORS(app)


@app.route("/api/carts/<id>", methods=["GET"])
def get_carts_by_id(id):


    result = ShoppingResource.get_by_key(id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/items/<id>", methods=["GET"])
def get_items_by_id(id):

    result = ShoppingResource.get_by_item_id(id)
    
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

