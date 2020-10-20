import uuid

import py2neo

ADDRESS = "localhost:7687"
AUTH = ("neo4j", "test")
NODE_LABEL = "User"
NODE_RELATIONSHIP = "SIMILAR"

graph = py2neo.Graph(address=ADDRESS, auth=AUTH)


def create_user(uid: str, name: str) -> bool:
    """
    takes user's unique id and name as inputs
    to insert as a node in the neo4j db

    note: it will create a new node, even if
    the uid and name combo already exists.

    Args:
     uid (string), user's id for reference
     name (string), user's name for reference

    Returns:
     boolean, confirming whether the User got created or not.
    """

    user = py2neo.Node(NODE_LABEL, uid=uid, name=name)
    graph.create(user)

    return graph.exists(user)


def create_similarity(from_uid: str, to_uid: str, conf: float) -> bool:
    """
    to create a relationship called "SIMILAR" between two nodes with
    confidence score as a property for that relationship.

    Args:
     from_uid (string), from-node's user id
     to_uid   (string), to-node's user id
     conf     (float), confidence score of similarity between users

    Returns:
     boolean, representing whether the relationship got inserted or not.
    """

    matcher = py2neo.NodeMatcher(graph)
    from_node = matcher.match(NODE_LABEL, uid=from_uid).first()
    to_node = matcher.match(NODE_LABEL, uid=to_uid).first()

    similar = py2neo.Relationship(from_node, NODE_RELATIONSHIP, to_node, conf=conf)
    graph.create(similar)

    return graph.exists(similar)


if __name__=="__main__":

    # only for raw sample examples

    from_uid = str(uuid.uuid4())
    to_uid = str(uuid.uuid4())

    print(create_user(uid=from_uid, name="yaswant"))
    print(create_user(uid=to_uid, name="bhavesh"))

    print(create_similarity(from_uid, to_uid, 0.78))

    from_uid = str(uuid.uuid4())
    to_uid = str(uuid.uuid4())

    print(create_user(uid=from_uid, name="rithumbhara"))
    print(create_user(uid=to_uid, name="shaaran"))

    print(create_similarity(from_uid, to_uid, 0.999))

    print(create_user(uid=str(uuid.uuid4()), name="jaivarsan"))
