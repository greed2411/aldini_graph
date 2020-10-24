"""
has functions which can be used for:
    * creating new nodes.
    * creating relationships between two existing nodes.
"""


import os
import uuid

import dotenv
import py2neo

# constants for user node label and relationship property value
NODE_LABEL = "User"
NODE_RELATIONSHIP = "SIMILAR"

dotenv.load_dotenv(verbose=True)

NEO4J_ADDRESS = os.getenv("NEO4J_ADDRESS")
NEO4J_AUTH_USERNAME=os.getenv("NEO4J_AUTH_USERNAME")
NEO4J_AUTH_PASSWORD=os.getenv("NEO4J_AUTH_PASSWORD")

AUTH = (NEO4J_AUTH_USERNAME, NEO4J_AUTH_PASSWORD)

graph = py2neo.Graph(address=NEO4J_ADDRESS, auth=AUTH)


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
