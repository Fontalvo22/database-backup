# Database backup

With this application you can setup your databases backups in short steps and storage locally or in as AWS S3 instance

### Prerequisites

This works using Docker, but if want it, you can run with a normal python installation; but without Docker you cant run Mysql, MongoDB, PostgreSQL and their initial data for testing

-   [python](https://www.python.org/)
-   [docker](https://hub.docker.com/) (optional)

### Installing

1.\_ open a terminal in the folder. Example:

    cd ~/database-backup

2.\_ if you have docker and docker-compose already installed, just run:

    docker-compose up -d --build

3.\_ If everything were fine, enter inside the container executing:

    docker exec -it app bash

4.\_ then, inside the container you can execute the script running:

    python index.py

Make sure you have your .env correctly configured.
The .env have default configuration for work with the database containers in docker-compose.yml

## For MongoDB when you are running with Docker

If you are trying to connect to MongoDB running on your local host, you must enter your connection string like this: mongodb://host.docker.internal:27017/
host.docker.internal:{port-numer}

is you are running it without Docker, just write as "localhost"

Remember use a password for mongoDB connections
