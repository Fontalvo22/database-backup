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

## Running the tests

Explain how to run the automated tests for this system

### Sample Tests

Explain what these tests test and why

    Give an example

### Style test

Checks if the best practices and the right coding style has been used.

    Give an example

## Deployment

Add additional notes to deploy this on a live system

## Built With

-   [Contributor Covenant](https://www.contributor-covenant.org/) - Used
    for the Code of Conduct
-   [Creative Commons](https://creativecommons.org/) - Used to choose
    the license

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [Semantic Versioning](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

-   **Billie Thompson** - _Provided README Template_ -
    [PurpleBooth](https://github.com/PurpleBooth)

See also the list of
[contributors](https://github.com/PurpleBooth/a-good-readme-template/contributors)
who participated in this project.

## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments

-   Hat tip to anyone whose code is used
-   Inspiration
-   etc
