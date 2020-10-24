# aldini-graph

[Neo4j](https://neo4j.com/) microservice for storing User details and their [typing biometrics](https://en.wikipedia.org/wiki/Keystroke_dynamics) relationships for aldini. This simple [flask](https://flask.palletsprojects.com/en/1.1.x/) microservice takes user information as JSON and inserts it into Neo4j. The project is an effort to demonstrate how we can use a graph db like [Neo4j](https://neo4j.com/) for empowering [TypingDNA](https://www.typingdna.com/) at scale. The demo of entire aldini will presented at [TypingDNA hackathon](https://typingdna.devpost.com/).

Presently we are using [Neo4j](https://neo4j.com/) and [Neo4j Browser User Interface](https://neo4j.com/developer/neo4j-browser/), which supports rich and intuitive relationship visualization.

This repostitory is intended as a microservice only, where aldini-backend can send relevant information over HTTP/1.1.

This code primarily uses [py2neo](https://py2neo.org/2020.0/) as neo4j driver, [flask](https://flask.palletsprojects.com/en/1.1.x/) as backend-http framework, [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) for production grade WSGI, [nginx](https://www.nginx.com/) as reverse-proxy and load-balancer. All thanks to [uwsgi-nginx-flask-docker](https://github.com/tiangolo/uwsgi-nginx-flask-docker). It was built using [Doom Emacs](https://github.com/hlissner/doom-emacs).


## Instructions on getting up and running

``` sh
→ docker build --rm . -t aldini-graph

→ docker-compose --env-file app/.env up 
```

## Instructions on how to use the endpoints

There are two important endpoints.

Note: replace the IP with your DOCKER IP though. You can find it as `inet addr` under `docker0` in ifconfig. Also the NGINX_PORT has been purposefully set as 8080 (in the .env) so that aldini-backend can run on default port 80.

1. `/api/add_user` which is used to create a new User node.

useful cURL requests for the same:

```sh
ozen:  ~/.../aldini_graph/app  |main ✓|
→ curl -d '{"uid":"123", "name":"bhavesh"}' -H "Content-Type: application/json" -X POST http://172.19.0.1:8080//api/add_user
{"created":true,"uid":"123"}

ozen:  ~/.../aldini_graph/app  |main ✓|
→ curl -d '{"uid":"456", "name":"yaswant"}' -H "Content-Type: application/json" -X POST http://172.19.0.1:8080/api/add_user
{"created":true,"uid":"456"}
```

2. `/api/add_match` which is used to create similarity relationship between two existing User nodes.

useful cURL requests for the same:

```sh
ozen:  ~/.../aldini_graph/app  |main ✓|
→ curl -d '{"from_uid":"456", "to_uid":"123" ,"conf":0.6}' -H "Content-Type: application/json" -X POST http://172.19.0.1:8080/api/add_match
{"conf":0.6,"created":true,"from_uid":"456","to_uid":"123"}
```


now run to your browser & open [http://localhost:7474](http://localhost:7474) to see visualzations using [Neo4j Browser User Interface](https://neo4j.com/developer/neo4j-browser/)


## Visualization Usage

For demo purposes these commands might be useful:

* show all User nodes and relationships

``` 
MATCH (n:User) RETURN n
```

* delete all nodes and relationships

``` 
MATCH (n:User) DETACH DELETE n
```

* show all Users relationships

```
MATCH (n:User)-[r:SIMILAR]-(:User) RETURN n
```


* show all relationships based on property's value

```
MATCH (n:User)-[r:SIMILAR]-(:User) WHERE r.conf > 0.8 RETURN n
```

