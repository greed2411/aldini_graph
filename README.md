# aldini-graph

Graph visualization component for aldini, for [TypingDNA hack](https://typingdna.devpost.com/).

Presently done using [Neo4j](https://neo4j.com/) and [Neo4j Browser User Interface](https://neo4j.com/developer/neo4j-browser/), which supports rich and intuitive relationship visualization.

This repostitory is intended as an example for how the backend can quickly borrow the code related to aldini-backend for maintaining user states.

This code primarily uses [py2neo](https://py2neo.org/2020.0/) and was built using [Doom Emacs](https://github.com/hlissner/doom-emacs).


## Instructions

``` sh
→ docker-compose up -d

# give couple of seconds

→ python n4j/create.py
```

now run to your browser & open [http://localhost:7474](http://localhost:7474)


## Usage

For demo purposes these commands might be useful:

* show all nodes and relationships

``` 
MATCH (n:User) RETURN n
```

* delete all nodes and relationships

``` 
MATCH (n:User) DETACH DELETE n
```

* show all relationships

```
MATCH (n:User)-[r:SIMILAR]-(:User) RETURN n
```


* show all relationships based on property's value

```
MATCH (n:User)-[r:SIMILAR]-(:User) WHERE r.conf > 0.8 RETURN n
```

