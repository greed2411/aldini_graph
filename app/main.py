"""
REST HTTP/1.1 endpoints for:
    * creating a new node for a user.
    * creating a new relationship between two user nodes.
"""

from flask import Flask, request, jsonify

from n4j.create import create_user, create_similarity

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/add_user", methods=["POST"])
def add_user():
    """
    api endpoint: /api/add_user
    request supported methods: POST
    content type: application/json

    request json data model: uid: string, name: string
    example for same: '{"uid":"123", "name":"yaswant"}'

    response json data model: uid: string, created: boolean
    example for same: '{"uid":"123", "created":true}'

    Note: uid is assumed to be unique in nature.
    """

    content = request.get_json()
    created_bool = create_user(uid=content["uid"], name=content["name"])
    resp_dict = {"uid": content["uid"], "created": created_bool}
    return jsonify(resp_dict)


@app.route("/api/add_match", methods=["POST"])
def add_match():
    """
    api endpoint: /api/add_match
    request supported methods: POST
    content type: application/json

    request json data model: from_uid: string, to_uid: string, conf: float
    example for same: '{"from_uid":"456", "to_uid":"123" ,"conf":0.6}'

    response json data model: from_uid: string, to_uid: string, conf: float ,created: boolean
    example for same: '{"from_uid":"456", "to_uid":"123" ,"conf":0.6, created:true}'

    Note: assumption is from_uid and to_uid are different, direction honestly doesn't matter in
    the end for our usecase.
    """

    content = request.get_json()
    created_bool = create_similarity(
        from_uid=content["from_uid"],
        to_uid=content["to_uid"],
        conf=content["conf"]
    )
    resp_dict = {
        "from_uid": content["from_uid"],
        "to_uid": content["to_uid"],
        "conf": content["conf"],
        "created": created_bool,
    }
    return jsonify(resp_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
